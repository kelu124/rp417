Claude
WeAct doesn’t say. The logic-analyzer firmware is only distributed as closed-source binaries, and the CNX write-up doesn’t name the sampling block either. But only one block on the CH32H417 is fast enough, so it’s almost certainly UHSIF: 
cnx-software

What it needs: USB 3.0: 4–200 MHz on 16 channels is 200 MHz × 2 bytes = 400 MB/s. 
cnx-software
UHSIF: the 32-bit width 125MHz general-purpose high-speed interface, rated at 500 MB/s, is the only block with that much bandwidth. 
github
DVP: at most 12 bits at 150 MHz, about 225 MB/s, so too slow for 16 ch at 200 MHz.
GPIO + timer + DMA (the STM32 BlackPill trick) tops out around tens of MS/s.
PIOC is far too slow.
One thing doesn’t add up: 200 MHz is above UHSIF’s rated 125 MHz clock. So WeAct is probably doing something clever, such as an internal sampling clock, double-edge capture, or overclocking. The USB2 limits (4–20 MHz @ 16 ch, 4–40 MHz @ 8 ch) are just the ~40 MB/s USB2 bottleneck. 
cnx-software

To confirm, check the schematic in the WeAct V2 repo (I couldn’t open it from here). If D0–D15 land on the UHSIF_PORT pins, that settles it.

This is good news for your 60 MSPS ADC: the same path gives you about 120 MB/s of headroom, and the board itself is a $10 USB 3.0 logic analyzer. It’s a handy CH32H417 dev board, and its Slot 2 user app is open source. 
cnx-software

Sources:

CNX Software – WeAct Logic Analyzer V2
openwch/ch32h417
I want to do a pulse echo board. So it means that on top of adc, i need to at zxactly the same time as my adc starts to get a pulse of 125ns on one logic, then nothing for 125us  then 125 us on another pin. How would i do it with the ch32 ?

Use one advanced timer in one-pulse mode to generate both pulses, and wire that same timer to the DVP so the ADC capture starts on the same edge. WCH timers are STM32-style, so this is the standard STM32 pattern. Check the CH32H417 reference manual for the exact timer clock limits.

1. Both pulses from one timer. I’ve read your sequence as: a 125 ns pulse on pin A at t = 0, a 125 µs gap, then a 125 µs pulse on pin B. Tell me if you meant something else.

Put the timer (TIM1/TIM8-style) in one-pulse mode, with ARR set to the end of the cycle.
CH1 in PWM mode: high from 0 to 125 ns, so CCR1 is 125 ns worth of ticks. That’s pin A.
CH2 in PWM mode 2 (inverted): low until 125.125 µs, then high until 250.125 µs. Set CCR2 to the turn-on time and ARR to the turn-off time. That’s pin B.
One trigger starts the counter, the hardware produces both edges, and there’s zero CPU jitter.
2. Start the ADC capture from the same timer.

Route a timer output (CH1 itself, or a CH3 gate) to DVP HSYNC/VSYNC, so DVP sees a frame/line become valid on the same edge that fires the pulse.
DVP then records N samples, set by the line length, by DMA into RAM. Size N for your echo window, e.g. 200 µs × 64 MSPS ≈ 12.8k samples.
3. Make the ADC clock and the timer share one clock. This is the key to getting “exactly the same time”.

If the ADC runs from its own oscillator, the pulse lands at a random point within a sample period: ±1 sample, about 16 ns.
Fix it by clocking the ADC from one oscillator and feeding that same clock into the timer’s external clock input (ETR / external clock mode 2). The timer then counts ADC samples, and the pulse is always aligned to the same sample.
At 64 MHz the numbers come out exact: 125 ns = 8 clocks and 125 µs = 8000 clocks, which fits a 16-bit timer. A 65 MSPS ADC like the AD9226 runs fine at 64 MHz. At 60 MHz, 125 ns would be 7.5 clocks, so you couldn’t hit it exactly.
4. Repetition rate. Fire the next shot either from a second timer acting as master (PRF timer → TRGO → slave starts the one-pulse timer) or from software after each DMA buffer arrives. Stream the buffers over USB3 vendor bulk, as before.

Hardware notes:

A 125 ns logic pulse goes into an HV pulser driver (e.g. MD1213 + TC6320, or an integrated pulser like the HV7361), not straight to the transducer.
The 125 µs pin B signal looks like a T/R-switch or damping control. Check its polarity and how fast the switch settles relative to when the first echoes arrive.
Keep the 64 MHz clock clean (a low-jitter oscillator, short routing), since clock jitter on the ADC turns directly into noise.
Could the adc run continiudly and stream to a usb3 device ?

Checking whether the USB3 link keeps up with streaming.
Yes. At 64 MSPS × 12 bits stored as 16-bit words you need 128 MB/s, and the CH32H417’s USB3 has been measured 450Mbytes per second. That leaves you a lot of headroom. The WeAct Logic Analyzer V2 already streams continuously at 400 MB/s on this chip, for up to about 45 s at 200 MHz with 16 channels, limited only by PC memory. Your case is about 3× easier. 
github
cnx-software

How to build it:

Capture: run DVP in continuous mode, so the ADC clock is PCLK and the “frame” never ends. DMA fills two or more buffers in a ring (ping-pong).
Buffering: with 896 KB of SRAM you could use, say, 4 × 128 KB buffers. That’s about 4 ms of data at 128 MB/s, enough to ride out host-side hiccups.
USB: when a buffer fills, send it out on a vendor bulk IN endpoint using USB3 bursts. Ideally DMA feeds the USB controller directly, so the CPU only shuffles buffer pointers.
Host side: use libusb with many asynchronous bulk transfers queued at once (16–32 × 64 KB or more). With a single synchronous read loop you’ll drop data. Writing 128 MB/s to an NVMe SSD is easy, but not to an HDD or SD card.
Things to watch:

No gaps: verify that DVP really does run without gaps between lines or frames in continuous mode. If it doesn’t, try UHSIF. Test this first by putting a counter pattern on the ADC data lines, or by feeding a sine wave and checking for discontinuities.
Packing: to cut bandwidth by 25% you can pack 12-bit samples down to 1.5 bytes (96 MB/s), but that costs CPU. At 128 MB/s you don’t need it.
USB2 fallback: it can’t sustain this rate. Detect it and drop to burst mode, or decimate the data.
Marking shots: for pulse-echo, flag where each shot starts in the stream. For example, put the pulse trigger on a spare DVP data bit (use bits 13–15 if you capture 16 bits) or log the sample counter at each trigger. Then you can continuously stream and cut the data into shots on the PC.
That last point means you don’t need the gated-capture scheme from before. Stream everything, and let the PC find each shot from the marker.


Fable 5.2 is here, and you have 3 free Fable limit resets for more room to explore. Use them by Mar 9, 2027, 8:59 AM GMT+1.


Claude is AI and can make mistakes.

