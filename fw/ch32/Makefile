# rp417 CH32H417MEU6 firmware (ch32fun, D71)
#
#   make build                 # -> rp417_ch32.elf/.bin/.hex
#   make flash                 # minichlink (RP2350 funprog programmer, D11)
#
# ch32fun comes from the reference clone (projects/clone.sh) unless CH32FUN is given.

all : build

TARGET := rp417_ch32
TARGET_MCU ?= CH32H417
CH32FUN ?= $(abspath ../../projects/tools/ch32fun/ch32fun)

ADDITIONAL_C_FILES :=
EXTRA_CFLAGS := -Wextra -Wno-unused-parameter -Wno-cpp

include $(CH32FUN)/ch32fun.mk

flash : cv_flash
clean : cv_clean
