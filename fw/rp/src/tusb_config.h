#pragma once

// Composite device: CDC0 = console, CDC1 = CH32 USART1 bridge, HID = funprog programmer (minichlink).
#define CFG_TUSB_RHPORT0_MODE   OPT_MODE_DEVICE
#define CFG_TUSB_OS             OPT_OS_PICO
#define CFG_TUD_ENDPOINT0_SIZE  64

#define CFG_TUD_CDC             2
#define CFG_TUD_HID             1
#define CFG_TUD_MSC             0
#define CFG_TUD_MIDI            0
#define CFG_TUD_VENDOR          0

#define CFG_TUD_CDC_RX_BUFSIZE  512
#define CFG_TUD_CDC_TX_BUFSIZE  1024
#define CFG_TUD_CDC_EP_BUFSIZE  64

// Feature reports up to 0xae = 264 bytes (+ report ID) go through this buffer on EP0.
#define CFG_TUD_HID_EP_BUFSIZE  272
