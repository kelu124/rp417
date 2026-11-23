// rp417 — CH32H417MEU6 bring-up firmware v0.1 (V3F core only)
//
// Talks to the RP2350 supervisor over USART1 (PA9 TX / PA10 RX, 115200 8N1) with the line protocol
// in fw/PROTOCOL.md, and gives the RP something to measure: LED, MCO on PB0, the 8-bit logic bus,
// the DVP sync inputs and the MARK line. Nothing here is hardware-tested yet (no board).
//
// Pin map: docs/pinmap.md (generated from hw/gen/build.py).

#include "ch32fun.h"
#include <stdio.h>
#include <string.h>

#define FW_VERSION "0.1"

// ---------------------------------------------------------------- pins (QFN88, D54..D66)
// RGB status LED D7, common anode on +3V3_CH -> active LOW (D62/D63)
#define PIN_LED_R PC2
#define PIN_LED_G PF0
#define PIN_LED_B PF1
// RP <-> CH32 logic bus LOGIC0..7 (D56): PD12 PD13 PD14 PD15 PD10 PD11 PC6 PC7
static const uint8_t logic_pins[8] = { PD12, PD13, PD14, PD15, PD10, PD11, PC6, PC7 };
#define PIN_HSYNC PA4   // driven by the RP (D37)
#define PIN_VSYNC PA5   // driven by the RP (D37)
#define PIN_MARK  PB14  // CH32 -> RP shot marker (TIM9_CH1 later, D56)
#define PIN_MCO   PB0   // MCO -> RP GPIO34 (frequency check)
#define PIN_SD_CD PD0   // microSD card detect
#define PIN_UART_TX PA9 // USART1, AF7 (DS V1.9 pin table)
#define PIN_UART_RX PA10

// ---------------------------------------------------------------- time
static uint32_t millis( void )
{
	return SysTick->CNT / DELAY_MS_TIME;   // 32-bit SysTick wraps after ~10.7 s at HCLK; only used for deltas
}

// ---------------------------------------------------------------- USART1
// Same BRR formula as ch32fun's own UART printf for H41x (uartdemo example).
// ⚠️ To verify on hardware: USART1 kernel clock vs FUNCONF_SYSTEM_CORE_CLOCK (baud may be off by the HB divider).
static void uart_init( void )
{
	RCC->HB2PCENR |= RCC_HB2Periph_GPIOA | RCC_HB2Periph_USART1 | RCC_HB2Periph_AFIO;
	funPinAF( PIN_UART_TX, 7 );
	funPinMode( PIN_UART_TX, GPIO_CNF_OUT_PP_AF, GPIO_Speed_50MHz );
	funPinAF( PIN_UART_RX, 7 );
	funPinMode( PIN_UART_RX, GPIO_CNF_IN_PUPD, GPIO_Speed_10MHz );
	funDigitalWrite( PIN_UART_RX, FUN_HIGH );   // pull-up: RX idles high if the RP has it tri-stated

	USART1->CTLR1 = USART_WordLength_8b | USART_Parity_No | USART_Mode_Tx | USART_Mode_Rx;
	USART1->CTLR2 = USART_StopBits_1;
	USART1->CTLR3 = USART_HardwareFlowControl_None;
	USART1->BRR = UART_BRR;
	USART1->CTLR1 |= CTLR1_UE_Set;
}

int putchar( int c )
{
	while( !( USART1->STATR & USART_FLAG_TXE ) );
	USART1->DATAR = (uint8_t)c;
	return 1;
}

int _write( int fd, const char *buf, int size )
{
	for( int i = 0; i < size; i++ )
	{
		if( buf[i] == '\n' ) putchar( '\r' );
		putchar( buf[i] );
	}
	return size;
}

static int uart_getc( void )
{
	if( USART1->STATR & USART_FLAG_RXNE ) return USART1->DATAR & 0xff;
	return -1;
}

// ---------------------------------------------------------------- LED
static uint8_t led_override = 0xff;   // 0xff = heartbeat, else bit0 R, bit1 G, bit2 B

static void led_set( uint8_t rgb )
{
	funDigitalWrite( PIN_LED_R, ( rgb & 1 ) ? FUN_LOW : FUN_HIGH );
	funDigitalWrite( PIN_LED_G, ( rgb & 2 ) ? FUN_LOW : FUN_HIGH );
	funDigitalWrite( PIN_LED_B, ( rgb & 4 ) ? FUN_LOW : FUN_HIGH );
}

// ---------------------------------------------------------------- MCO (PB0, AF0 = MCO, as ch32fun blink_and_mco)
static const struct { const char *name; uint32_t sel; } mco_srcs[] = {
	{ "off", RCC_CFGR0_MCO_NOCLOCK },
	{ "sys", RCC_CFGR0_MCO_SYSCLK },   // 400 MHz: too fast for the RP counter, scope only
	{ "hsi", RCC_CFGR0_MCO_HSI },
	{ "hse", RCC_CFGR0_MCO_HSE },      // 25 MHz crystal: default, measured by the RP 'freq' command
	{ "pll2", RCC_CFGR0_MCO_PLL_DIV2 },
};

static int mco_set( const char *name )
{
	for( unsigned i = 0; i < sizeof( mco_srcs ) / sizeof( mco_srcs[0] ); i++ )
	{
		if( strcmp( name, mco_srcs[i].name ) ) continue;
		RCC->CFGR0 = ( RCC->CFGR0 & ~RCC_CFGR0_MCO ) | mco_srcs[i].sel;
		return 0;
	}
	return -1;
}

// ---------------------------------------------------------------- logic bus
static void logic_hiz( void )
{
	for( int i = 0; i < 8; i++ ) funPinMode( logic_pins[i], GPIO_CNF_IN_FLOATING, GPIO_Speed_10MHz );
}

static void logic_out( uint8_t v )
{
	for( int i = 0; i < 8; i++ )
	{
		funDigitalWrite( logic_pins[i], ( v >> i ) & 1 );
		funPinMode( logic_pins[i], GPIO_CNF_OUT_PP, GPIO_Speed_50MHz );
	}
}

static uint8_t logic_in( void )
{
	uint8_t v = 0;
	for( int i = 0; i < 8; i++ ) v |= funDigitalRead( logic_pins[i] ) << i;
	return v;
}

// ---------------------------------------------------------------- parsing (no libc: ch32fun links -nostdlib)
static char *next_word( char **p )
{
	char *s = *p;
	while( *s == ' ' || *s == '\t' ) s++;
	if( !*s ) { *p = s; return NULL; }
	char *w = s;
	while( *s && *s != ' ' && *s != '\t' ) s++;
	if( *s ) *s++ = 0;
	*p = s;
	return w;
}

static uint32_t parse_hex( const char *s )
{
	uint32_t v = 0;
	if( s[0] == '0' && ( s[1] == 'x' || s[1] == 'X' ) ) s += 2;
	for( ; *s; s++ )
	{
		char c = *s | 0x20;
		if( c >= '0' && c <= '9' ) v = v * 16 + ( c - '0' );
		else if( c >= 'a' && c <= 'f' ) v = v * 16 + ( c - 'a' + 10 );
		else break;
	}
	return v;
}

// ---------------------------------------------------------------- commands (fw/PROTOCOL.md)
static void cmd_help( void )
{
	printf( "ping | ver | clk | led <0-7|hb> | mco <off|sys|hsi|hse|pll2> |\n"
	        "lin | lout <hex> | lz | sync | mark <0|1|z> | sd | help\n" );
}

static void handle_line( char *line )
{
	char *cmd = next_word( &line );
	char *arg = next_word( &line );
	if( !cmd ) return;

	if( !strcmp( cmd, "ping" ) ) printf( "pong\n" );
	else if( !strcmp( cmd, "ver" ) ) printf( "rp417-ch32 " FW_VERSION " " __DATE__ " " __TIME__ "\n" );
	else if( !strcmp( cmd, "clk" ) )
		printf( "sysclk %lu hse %lu cfgr0 %08lx\n", (unsigned long)FUNCONF_SYSTEM_CORE_CLOCK,
		        (unsigned long)HSE_VALUE, (unsigned long)RCC->CFGR0 );
	else if( !strcmp( cmd, "led" ) )
	{
		if( !arg ) { printf( "err arg\n" ); return; }
		led_override = strcmp( arg, "hb" ) ? ( parse_hex( arg ) & 7 ) : 0xff;
		if( led_override != 0xff ) led_set( led_override );
	}
	else if( !strcmp( cmd, "mco" ) )
	{
		if( !arg || mco_set( arg ) ) { printf( "err arg\n" ); return; }
	}
	else if( !strcmp( cmd, "lin" ) ) printf( "logic %02x\n", logic_in() );
	else if( !strcmp( cmd, "lout" ) )
	{
		if( !arg ) { printf( "err arg\n" ); return; }
		logic_out( parse_hex( arg ) );
	}
	else if( !strcmp( cmd, "lz" ) ) logic_hiz();
	else if( !strcmp( cmd, "sync" ) )
		printf( "hsync %d vsync %d\n", funDigitalRead( PIN_HSYNC ), funDigitalRead( PIN_VSYNC ) );
	else if( !strcmp( cmd, "mark" ) )
	{
		if( !arg ) { printf( "err arg\n" ); return; }
		if( arg[0] == 'z' ) funPinMode( PIN_MARK, GPIO_CNF_IN_FLOATING, GPIO_Speed_10MHz );
		else
		{
			funDigitalWrite( PIN_MARK, arg[0] == '1' );
			funPinMode( PIN_MARK, GPIO_CNF_OUT_PP, GPIO_Speed_50MHz );
		}
	}
	else if( !strcmp( cmd, "sd" ) ) printf( "sd_cd %d\n", funDigitalRead( PIN_SD_CD ) );
	else if( !strcmp( cmd, "help" ) ) cmd_help();
	else { printf( "err unknown %s\n", cmd ); return; }
	printf( "ok\n" );
}

// ---------------------------------------------------------------- main
int main( void )
{
	SystemInit();
	funGpioInitAll();

	// Safe defaults: every RP-facing line is an input (D29) until the RP asks otherwise.
	led_set( 0 );
	funPinMode( PIN_LED_R, GPIO_CNF_OUT_PP, GPIO_Speed_10MHz );
	funPinMode( PIN_LED_G, GPIO_CNF_OUT_PP, GPIO_Speed_10MHz );
	funPinMode( PIN_LED_B, GPIO_CNF_OUT_PP, GPIO_Speed_10MHz );
	logic_hiz();
	funPinMode( PIN_HSYNC, GPIO_CNF_IN_FLOATING, GPIO_Speed_10MHz );
	funPinMode( PIN_VSYNC, GPIO_CNF_IN_FLOATING, GPIO_Speed_10MHz );
	funPinMode( PIN_MARK, GPIO_CNF_IN_FLOATING, GPIO_Speed_10MHz );
	funPinMode( PIN_SD_CD, GPIO_CNF_IN_PUPD, GPIO_Speed_10MHz );
	funDigitalWrite( PIN_SD_CD, FUN_HIGH );   // pull-up

	// MCO = HSE (25 MHz) on PB0 so the RP can check the crystal and that we run.
	funPinAF( PIN_MCO, 0 );
	funPinMode( PIN_MCO, GPIO_CNF_OUT_PP_AF, GPIO_Speed_100MHz );
	mco_set( "hse" );

	uart_init();
	printf( "\n# rp417-ch32 " FW_VERSION " boot\n" );

	char line[64];
	int len = 0;
	uint32_t last = millis();
	int hb = 0;

	while( 1 )
	{
		int c = uart_getc();
		if( c >= 0 )
		{
			if( c == '\r' || c == '\n' )
			{
				line[len] = 0;
				if( len ) handle_line( line );
				len = 0;
			}
			else if( len < (int)sizeof( line ) - 1 ) line[len++] = c;
		}

		uint32_t now = millis();
		if( now - last >= 500 )
		{
			last = now;
			hb = !hb;
			if( led_override == 0xff ) led_set( hb ? 2 : 0 );   // green heartbeat
		}
	}
}
