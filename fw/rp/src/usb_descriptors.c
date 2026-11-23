// USB descriptors: CDC0 console + CDC1 CH32 UART bridge + HID funprog programmer.
//
// VID:PID 1209:0001 is the pid.codes *test* PID — fine on our own bench, to replace with an
// allocated PID before the firmware is shared. minichlink: `minichlink -c 0x12090001 -C funprog ...`
#include "tusb.h"
#include "pico/unique_id.h"
#include <string.h>

#define USB_VID 0x1209
#define USB_PID 0x0001
#define USB_BCD 0x0200

enum { ITF_CDC0 = 0, ITF_CDC0_DATA, ITF_CDC1, ITF_CDC1_DATA, ITF_HID, ITF_COUNT };

#define EP_CDC0_NOTIF 0x81
#define EP_CDC0_OUT   0x02
#define EP_CDC0_IN    0x82
#define EP_CDC1_NOTIF 0x83
#define EP_CDC1_OUT   0x04
#define EP_CDC1_IN    0x84
#define EP_HID_IN     0x85

static const tusb_desc_device_t desc_device = {
	.bLength = sizeof(tusb_desc_device_t),
	.bDescriptorType = TUSB_DESC_DEVICE,
	.bcdUSB = USB_BCD,
	.bDeviceClass = TUSB_CLASS_MISC,          // IAD
	.bDeviceSubClass = MISC_SUBCLASS_COMMON,
	.bDeviceProtocol = MISC_PROTOCOL_IAD,
	.bMaxPacketSize0 = CFG_TUD_ENDPOINT0_SIZE,
	.idVendor = USB_VID,
	.idProduct = USB_PID,
	.bcdDevice = 0x0001,
	.iManufacturer = 1,
	.iProduct = 2,
	.iSerialNumber = 3,
	.bNumConfigurations = 1,
};

uint8_t const *tud_descriptor_device_cb(void) { return (uint8_t const *)&desc_device; }

// HID report descriptor: the funprog feature reports (same IDs/sizes as cnlohr's ch570funprog).
static const uint8_t desc_hid_report[] = {
	0x06, 0x00, 0xff,        // Usage Page (Vendor 0xFF00)
	0x09, 0x01,              // Usage 1
	0x15, 0x00,              // Logical Min 0
	0x26, 0xff, 0x00,        // Logical Max 255
	0x75, 0x08,              // Report Size 8
	0xa1, 0x01,              // Collection (Application)
	0x85, 0xaa, 0x95, 7,   0x09, 0x01, 0xb2, 0x02, 0x01,   // ID 0xaa, 7 bytes, Feature (buffered bytes)
	0x85, 0xab, 0x95, 63,  0x09, 0x01, 0xb2, 0x02, 0x01,   // ID 0xab, 63
	0x85, 0xac, 0x95, 127, 0x09, 0x01, 0xb2, 0x02, 0x01,   // ID 0xac, 127
	0x85, 0xad, 0x95, 78,  0x09, 0x01, 0xb2, 0x02, 0x01,   // ID 0xad, 78
	0x85, 0xae, 0x96, 0x07, 0x01, 0x09, 0x01, 0xb2, 0x02, 0x01,   // ID 0xae, 263
	0xc0,                    // End Collection
};

uint8_t const *tud_hid_descriptor_report_cb(uint8_t instance)
{
	(void)instance;
	return desc_hid_report;
}

#define CONFIG_TOTAL_LEN (TUD_CONFIG_DESC_LEN + 2 * TUD_CDC_DESC_LEN + TUD_HID_DESC_LEN)

static const uint8_t desc_config[] = {
	TUD_CONFIG_DESCRIPTOR(1, ITF_COUNT, 0, CONFIG_TOTAL_LEN, 0x00, 100),
	TUD_CDC_DESCRIPTOR(ITF_CDC0, 4, EP_CDC0_NOTIF, 8, EP_CDC0_OUT, EP_CDC0_IN, 64),
	TUD_CDC_DESCRIPTOR(ITF_CDC1, 5, EP_CDC1_NOTIF, 8, EP_CDC1_OUT, EP_CDC1_IN, 64),
	TUD_HID_DESCRIPTOR(ITF_HID, 6, HID_ITF_PROTOCOL_NONE, sizeof(desc_hid_report), EP_HID_IN, 64, 10),
};

uint8_t const *tud_descriptor_configuration_cb(uint8_t index)
{
	(void)index;
	return desc_config;
}

static char serial[2 * PICO_UNIQUE_BOARD_ID_SIZE_BYTES + 1];

static const char *const strings[] = {
	NULL,                       // 0: language (handled below)
	"rp417",                    // 1: manufacturer
	"rp417 supervisor",         // 2: product
	serial,                     // 3: serial = RP2350 unique ID
	"rp417 console",            // 4: CDC0
	"rp417 CH32 UART",          // 5: CDC1
	"rp417 CH32 programmer",    // 6: HID
};

static uint16_t desc_str[48];

uint16_t const *tud_descriptor_string_cb(uint8_t index, uint16_t langid)
{
	(void)langid;
	size_t n;
	if (index == 0) {
		desc_str[1] = 0x0409;
		n = 1;
	} else {
		if (index >= sizeof strings / sizeof strings[0]) return NULL;
		if (index == 3 && !serial[0]) pico_get_unique_board_id_string(serial, sizeof serial);
		const char *s = strings[index];
		n = strlen(s);
		if (n > 47) n = 47;
		for (size_t i = 0; i < n; i++) desc_str[1 + i] = (uint8_t)s[i];
	}
	desc_str[0] = (uint16_t)((TUSB_DESC_STRING << 8) | (2 * n + 2));
	return desc_str;
}
