cmake_minimum_required(VERSION 3.13)

# rp417 RP2354B supervisor firmware (D71).
#   mkdir build && cd build && cmake .. && make      -> rp417_rp.uf2
# PICO_SDK_PATH must point at pico-sdk >= 2.1. CH32FUN_PATH defaults to the reference clone.

set(PICO_BOARD rp417)
set(PICO_BOARD_HEADER_DIRS ${CMAKE_CURRENT_LIST_DIR}/boards)
set(PICO_PLATFORM rp2350-arm-s)

include(pico_sdk_import.cmake)

project(rp417_rp C CXX ASM)
set(CMAKE_C_STANDARD 11)

pico_sdk_init()

set(CH32FUN_PATH ${CMAKE_CURRENT_LIST_DIR}/../../projects/tools/ch32fun CACHE PATH "ch32fun checkout")
if(NOT EXISTS ${CH32FUN_PATH}/minichlink/funprog/funprog_logic.h)
	message(FATAL_ERROR "ch32fun not found at ${CH32FUN_PATH} (run projects/clone.sh or set CH32FUN_PATH)")
endif()

add_executable(rp417_rp
	src/main.c
	src/board.c
	src/si5351.c
	src/chlink.c
	src/console.c
	src/programmer.c
	src/usb_descriptors.c
)

pico_generate_pio_header(rp417_rp ${CMAKE_CURRENT_LIST_DIR}/src/edgecount.pio)

target_include_directories(rp417_rp PRIVATE
	${CMAKE_CURRENT_LIST_DIR}/src
	${CMAKE_CURRENT_LIST_DIR}/funprog
	${CH32FUN_PATH}/minichlink/funprog
)

target_compile_options(rp417_rp PRIVATE -Wall -Wno-unused-function)

target_link_libraries(rp417_rp
	pico_stdlib
	pico_unique_id
	hardware_adc
	hardware_i2c
	hardware_pio
	hardware_uart
	tinyusb_device
	tinyusb_board
)

pico_enable_stdio_usb(rp417_rp 0)
pico_enable_stdio_uart(rp417_rp 0)
pico_add_extra_outputs(rp417_rp)
