// rp417 funprog programmer (D11): minichlink on the host talks HID feature reports 0xaa..0xae,
// the funprog core (ch32fun/minichlink/funprog) turns them into SWIO/RVSWD transactions.
//
// Report handling follows cnlohr's ch570funprog (all IDs -> HandleCommandBuffer) and the ESP32-S2
// trick for TinyUSB: the reply starts with a length byte where TinyUSB has put the report ID.
#include "funprog_config.h"
#include "funprog_port.h"
#include "funprog_rvswdio.h"
#include "bitbang_rvswdio.h"
#include "funprog_logic.h"

#include "tusb.h"
#include "board.h"
#include "programmer.h"

#define PROG_IDLE_MS 3000

static uint8_t scratch[272];
static uint8_t retbuff[272];
static bool attached;
static absolute_time_t last_cmd;

bool prog_is_attached(void) { return attached; }

void prog_attach(void)
{
	if (!ch_power_is_on()) ch_power_on();
	usb_sel_swd(true);
	attached = true;
	last_cmd = get_absolute_time();
}

void prog_activity(bool busy)
{
	board_led(busy ? LED_B : (attached ? LED_B | LED_G : LED_G));
}

void prog_task(void)
{
	if (attached && absolute_time_diff_us(last_cmd, get_absolute_time()) > PROG_IDLE_MS * 1000) {
		usb_sel_swd(false);   // PB8/PB9 back to the J1 USB connector, SWD pins high-Z
		attached = false;
		board_led(LED_G);
	}
}

void tud_hid_set_report_cb(uint8_t instance, uint8_t report_id, hid_report_type_t report_type,
                           uint8_t const *buffer, uint16_t bufsize)
{
	(void)instance;
	(void)report_type;
	if (report_id < 0xaa || report_id > 0xae) return;
	if (bufsize > sizeof scratch - 1) bufsize = sizeof scratch - 1;
	scratch[0] = report_id;
	memcpy(scratch + 1, buffer, bufsize);
	memset(retbuff, 0, sizeof retbuff);
	last_cmd = get_absolute_time();
	HandleCommandBuffer(scratch, bufsize + 1, retbuff, sizeof retbuff - 1);
	last_cmd = get_absolute_time();
}

uint16_t tud_hid_get_report_cb(uint8_t instance, uint8_t report_id, hid_report_type_t report_type,
                               uint8_t *buffer, uint16_t reqlen)
{
	(void)instance;
	(void)report_type;
	if (report_id < 0xaa || report_id > 0xae) return 0;
	// buffer[-1] holds the report ID TinyUSB inserted; minichlink expects retbuff[0] (length) there.
	uint16_t n = reqlen + 1;
	if (n > sizeof retbuff) n = sizeof retbuff;
	memcpy(buffer - 1, retbuff, n);
	return n - 1;
}

// Console 'swd' probe: attach, run the funprog init (SWIO then RVSWD), read DMSTATUS.
int prog_probe(int *opmode, uint32_t *dmstatus)
{
	struct SWIOState st;
	memset(&st, 0, sizeof st);
	prog_attach();
	int r = InitializeSWDSWIO(&st);
	*opmode = st.opmode;
	*dmstatus = 0;
	if (r == 0 && MCFReadReg32(&st, DMSTATUS, dmstatus) != 0) r = -100;
	last_cmd = get_absolute_time();
	return r;
}
