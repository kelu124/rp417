#ifndef FUNPROG_CONFIG_H
#define FUNPROG_CONFIG_H

// rp417: RP2354B as a ch32fun "funprog" programmer for the on-board CH32H417 (D11).
// Core: projects/tools/ch32fun/minichlink/funprog (funprog_rvswdio.h + funprog_logic.h).

#define DEBUG_PRINT              0

#define CH5xx_SUPPORT            0   // target is a CH32H417, not a CH5xx
#define CH5xx_EEPROM             0
#define CH5xx_OPTIONS            0
#define CH5xx_UNLOCK             0
#define UPDI_SUPPORT             0
#define USB_HID_INTERFACE        1
#define USB_VENDOR_INTERFACE     0
#define WEBSOCKET_INTERFACE      0
#define WEB_INTERFACE            0
#define BLE_INTERFACE            0
#define MCO_SUPPORT              0

#define PROGRAMMER_TYPE_UNKNOWN  0
#define PROGRAMMER_TYPE_ESP32S2  1
#define PROGRAMMER_TYPE_CH32V003 2
#define PROGRAMMER_TYPE_CH570    3
#define PROGRAMMER_TYPE_ESP32    4
#define PROGRAMMER_TYPE_SWADGE   5

// No rp417 type in minichlink yet; UNKNOWN keeps the generic (v5, small-buffer) host path.
#define PROGRAMMER_TYPE          PROGRAMMER_TYPE_UNKNOWN

#define HAS_MCO                  (MCO_SUPPORT << 12)
#define HAS_BLE                  (BLE_INTERFACE << 11)
#define HAS_WEB_UI               (WEB_INTERFACE << 10)
#define HAS_WEBSOCKET            (WEBSOCKET_INTERFACE << 9)
#define HAS_USB_VENDOR           (USB_VENDOR_INTERFACE << 8)
#define HAS_USB_HID              (USB_HID_INTERFACE << 7)
#define HAS_UPDI_SUPPORT         (UPDI_SUPPORT << 5)
#define HAS_CH5xx_UNLOCK         (CH5xx_UNLOCK << 3)
#define HAS_CH5xx_OPTIONS        (CH5xx_OPTIONS << 2)
#define HAS_CH5xx_EEPROM         (CH5xx_EEPROM << 1)
#define HAS_CH5xx_SUPPORT        (CH5xx_SUPPORT << 0)

#define CAPABILITIES (HAS_USB_HID)

#define MAX_IN_TIMEOUT           1000

#endif
