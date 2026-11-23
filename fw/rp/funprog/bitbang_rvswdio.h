// RP2350 bit-bang layer for funprog: 1-wire SWIO and 2-wire RVSWD on GPIO35 (SWIO/SWDIO) and
// GPIO36 (SWCLK), routed to CH32 PB9/PB8 by the TS3USB221A when USB_SEL = 1 (D14/D26).
//
// Timings follow cnlohr's ch570funprog (bitbang_rvswdio_ch57x.h) comments, expressed in ns here.
// ⚠️ Not hardware-tested (no board yet). Rev A has NO pull-up on SWIO (net SWIO_RP = U2.44 + U4.4 only);
// 1-wire SWIO reads rely on the RP internal pull-up + a short active precharge (see ReadBitSWIO).
// funprog tries SWIO first and falls back to 2-wire RVSWD, which does not need the pull-up.
#ifndef BITBANG_RVSWDIO_RP2350_H
#define BITBANG_RVSWDIO_RP2350_H

#include "hardware/gpio.h"
#include "hardware/clocks.h"
#include "hardware/sync.h"

#define BB_SWD PIN_SWIO
#define BB_SWC PIN_SWCLK

// ns -> sys clock cycles (clk_sys 150 MHz default)
#define BB_CYC(ns) ((uint32_t)(((uint64_t)(ns) * SYS_CLK_HZ) / 1000000000ull))

// SWIO (1-wire)
#define SWIO_1_LOW_NS   250   // valid ~100..500 ns
#define SWIO_0_LOW_NS   900   // valid ~500..2000 ns
#define SWIO_HIGH_NS    250
#define SWIO_RD_LOW_NS  100   // host start pulse
#define SWIO_RD_PRE_NS  15    // active precharge high after the start pulse (no external pull-up)
#define SWIO_RD_SMP_NS  250   // release -> sample
#define SWIO_RD_REC_NS  400   // recovery, line high
// RVSWD (2-wire): half clock period
#define RVSWD_HALF_NS   250   // ~2 MHz

static uint32_t bb_irq;

static inline void bb_delay(uint32_t cycles) { busy_wait_at_least_cycles(cycles); }

static inline void bb_swd_out(int v)
{
	gpio_put(BB_SWD, v);
	gpio_set_dir(BB_SWD, GPIO_OUT);
}

static inline void bb_swd_in(void) { gpio_set_dir(BB_SWD, GPIO_IN); }

static inline void bb_lock(void) { bb_irq = save_and_disable_interrupts(); }
static inline void bb_unlock(void) { restore_interrupts(bb_irq); }

static inline uint32_t rvswd_half(struct SWIOState *state)
{
	return BB_CYC(state->t1coeff ? state->t1coeff : RVSWD_HALF_NS);
}

// ---------------------------------------------------------------- SWIO (1-wire)
static inline void Send1BitSWIO(struct SWIOState *state)
{
	(void)state;
	bb_swd_out(0);
	bb_delay(BB_CYC(SWIO_1_LOW_NS));
	gpio_put(BB_SWD, 1);
	bb_delay(BB_CYC(SWIO_HIGH_NS));
}

static inline void Send0BitSWIO(struct SWIOState *state)
{
	(void)state;
	bb_swd_out(0);
	bb_delay(BB_CYC(SWIO_0_LOW_NS));
	gpio_put(BB_SWD, 1);
	bb_delay(BB_CYC(SWIO_HIGH_NS));
}

static inline int ReadBitSWIO(struct SWIOState *state)
{
	(void)state;
	bb_swd_out(0);
	bb_delay(BB_CYC(SWIO_RD_LOW_NS));
	gpio_put(BB_SWD, 1);                // short precharge: no external pull-up on rev A
	bb_delay(BB_CYC(SWIO_RD_PRE_NS));
	bb_swd_in();
	bb_delay(BB_CYC(SWIO_RD_SMP_NS));
	int r = gpio_get(BB_SWD);
	bb_delay(BB_CYC(SWIO_RD_REC_NS));
	bb_swd_out(1);
	return r;
}

// ---------------------------------------------------------------- RVSWD (2-wire)
static inline void SendBitRVSWD(struct SWIOState *state, int val)
{
	// SWC high on entry
	gpio_put(BB_SWC, 0);
	bb_swd_out(!!val);
	bb_delay(rvswd_half(state));
	gpio_put(BB_SWC, 1);
	bb_delay(rvswd_half(state));
}

static inline int ReadBitRVSWD(struct SWIOState *state)
{
	bb_swd_in();
	gpio_put(BB_SWC, 0);
	bb_delay(rvswd_half(state));
	int r = gpio_get(BB_SWD);
	gpio_put(BB_SWC, 1);
	bb_delay(rvswd_half(state));
	return r;
}

static void SWDStop(struct SWIOState *state)
{
	(void)state;
	gpio_put(BB_SWC, 0);
	bb_delay(BB_CYC(50));
	bb_swd_out(0);
	bb_delay(BB_CYC(50));
	gpio_put(BB_SWC, 1);
	bb_delay(BB_CYC(50));
	gpio_put(BB_SWD, 1);
	busy_wait_us_32(2);
}

static void RVFinishRegop(struct SWIOState *state)
{
	ReadBitRVSWD(state);
	ReadBitRVSWD(state);
	ReadBitRVSWD(state);
	SendBitRVSWD(state, 1);   // 0 for register, 1 for value
	SendBitRVSWD(state, 0);
	SWDStop(state);
	bb_unlock();
}

// ---------------------------------------------------------------- register access
static void MCFWriteReg32(struct SWIOState *state, uint8_t command, uint32_t value)
{
	if (state->opmode == 1) {
		bb_lock();
		Send1BitSWIO(state);
		for (uint32_t mask = 1 << 6; mask; mask >>= 1)
			(command & mask) ? Send1BitSWIO(state) : Send0BitSWIO(state);
		Send1BitSWIO(state);   // write
		for (uint32_t mask = 1u << 31; mask; mask >>= 1)
			(value & mask) ? Send1BitSWIO(state) : Send0BitSWIO(state);
		bb_unlock();
		busy_wait_us_32(1);
	} else if (state->opmode == 2) {
		bb_lock();
		bb_swd_out(0);   // start
		bb_delay(BB_CYC(50));
		int parity = 1;
		for (uint32_t mask = 1 << 6; mask; mask >>= 1) {
			int v = !!(command & mask);
			parity ^= v;
			SendBitRVSWD(state, v);
		}
		SendBitRVSWD(state, 1);   // write
		SendBitRVSWD(state, parity);
		ReadBitRVSWD(state);
		ReadBitRVSWD(state);
		ReadBitRVSWD(state);
		SendBitRVSWD(state, 0);   // register
		SendBitRVSWD(state, 0);
		parity = 0;
		for (uint32_t mask = 1u << 31; mask; mask >>= 1) {
			int v = !!(value & mask);
			parity ^= v;
			SendBitRVSWD(state, v);
		}
		SendBitRVSWD(state, parity);
		RVFinishRegop(state);
	}
}

static int MCFReadReg32(struct SWIOState *state, uint8_t command, uint32_t *value)
{
	if (state->opmode == 1) {
		bb_lock();
		Send1BitSWIO(state);
		for (uint32_t mask = 1 << 6; mask; mask >>= 1)
			(command & mask) ? Send1BitSWIO(state) : Send0BitSWIO(state);
		Send0BitSWIO(state);   // read
		uint32_t rv = 0;
		for (int i = 0; i < 32; i++) rv = (rv << 1) | ReadBitSWIO(state);
		ReadBitSWIO(state);    // check bit
		bb_unlock();
		busy_wait_us_32(1);
		*value = rv;
		return 0;
	} else if (state->opmode == 2) {
		bb_lock();
		bb_swd_out(0);
		bb_delay(BB_CYC(50));
		int parity = 0;
		for (uint32_t mask = 1 << 6; mask; mask >>= 1) {
			int v = !!(command & mask);
			parity ^= v;
			SendBitRVSWD(state, v);
		}
		SendBitRVSWD(state, 0);   // read
		SendBitRVSWD(state, parity);
		ReadBitRVSWD(state);
		ReadBitRVSWD(state);
		ReadBitRVSWD(state);
		SendBitRVSWD(state, 0);
		SendBitRVSWD(state, 0);
		uint32_t rv = 0;
		parity = 0;
		for (int i = 0; i < 32; i++) {
			int r = ReadBitRVSWD(state);
			rv = (rv << 1) | r;
			parity ^= r;
		}
		*value = rv;
		int bad = ReadBitRVSWD(state) != parity;
		RVFinishRegop(state);
		return bad ? -1 : 0;
	}
	return -1;
}

// ---------------------------------------------------------------- IO setup
static inline void ConfigureIOForRVSWIO(struct SWIOState *state)
{
	(void)state;
	gpio_init(BB_SWD);
	gpio_pull_up(BB_SWD);
	gpio_set_drive_strength(BB_SWD, GPIO_DRIVE_STRENGTH_4MA);
	gpio_set_slew_rate(BB_SWD, GPIO_SLEW_RATE_FAST);
	bb_swd_out(1);
	gpio_init(BB_SWC);                  // SWCLK idle as input in 1-wire mode
	gpio_disable_pulls(BB_SWC);
}

static inline void ConfigureIOForRVSWD(struct SWIOState *state)
{
	(void)state;
	gpio_init(BB_SWC);
	gpio_put(BB_SWC, 1);
	gpio_set_dir(BB_SWC, GPIO_OUT);
	gpio_set_drive_strength(BB_SWC, GPIO_DRIVE_STRENGTH_4MA);
	gpio_init(BB_SWD);
	gpio_pull_up(BB_SWD);
	bb_swd_out(1);
}

#endif
