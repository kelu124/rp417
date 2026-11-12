CH32H417 UHSIF Development Reference Manual                                                 https://wch-ic.com

CH32H417 Universal High-speed Interface (UHSIF) Development
Datasheet
Version: V1.0
https://wch-ic.com
1.  Overview
The chip incorporates a set of universal high-speed interfaces (UHSIF), which can transmit clock up to 125MHz,
support data widths of 8-, 16-, 24-, or 32-bit, with a theoretical maximum data rate of 500Mbytes/s.

2.  Features
  Support master and slave modes
  Support 8-, 16-, 24-, and 32-bit data bus widths
  Configurable clock frequency, up to 125MHz
  Configurable clock sampling edge and data output edge
  Flexible mapping of address and control pins

3.  Pin Information
3.1. Pin Definitions
The UHSIF peripheral supports up to 49 pins, including the UHSIF_CLK pin and the configurable interface pins
UHSIF_PORT[47:0].
The interface pins consist of 2 address pins, 14 control pins, and 32 data pins.
In standard applications, a 32-bit data width requires 44 pins; for 24-bit, 16-bit, and 8-bit data widths, simply
reduce the number of data pins accordingly. Refer to Table 3-1 for pin definitions.
If not all transmission lines (Line) are used, the number of SEL pins can be reduced accordingly. For example, if
only Line0 and Line1 are used, only the SEL0 pin is required. Specifically, if only Line0 is used, no SEL pin is
required. For information on transmission lines, refer to Section 4.1 Transmission Lines and Buffers.
Table 3-1 Pin definitions
Pin direction
| Pin name  | Pin type  |     |     | Pin function  |
| --------- | --------- | --- | --- | ------------- |
Host  Slave
| CS#  | Control  | O  I  | Chip selection signal, active low.       |     |
| ---- | -------- | ----- | ---------------------------------------- | --- |
| WR#  | Control  | O  I  | Write enable signal, active low.         |     |
| RD#  | Control  | O  I  | Read enable signal, active low.          |     |
| OE#  | Control  | O  I  | Slave output enable signal, active low.  |     |
EOP#  Control  O  I  Write end or write zero length packet signal, active low.
SEL[1:0]  Address  O  I  Address bus for internal transmission line selection.
| DATA[31:0]  | Data     | I/O  I/O  | 32-bit data bus.                  |     |
| ----------- | -------- | --------- | --------------------------------- | --- |
| PCLK        | Clock    | O  I      | Clock signal.                     |     |
| RDNE        | Control  | I  O      | Non-null signal in slave buffer.  |     |
| WRNF        | Control  | I  O      | Non-full signal in slave buffer.  |     |
V1.0                                               1

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
AF# Control I O Almost Full signal in slave buffer.
AE# Control I O Almost Empty signal in slave buffer.
3.2. Pin Mapping Description
Figure 3-1 UHSIF signal path
MCU I/O GGPPIIOO
UHSIF_PORT_RM
UHSIF peripheral
UHSIF_CLK UHSIF_PORT[47:0]
signals
API
configuration
UHSIF internal
Clock pin Control/Address/Data pin
signals
The UHSIF clock pin (PCLK) is permanently connected to UHSIF_CLK, while the remaining UHSIF pins can be
mapped to UHSIF_PORT[47:0]. DATA[31:0] can be mapped to UHSIF_PORT[31:0] or UHSIF_PORT[47:16]; in
either mapping scheme, the address and control pins can be flexibly configured on the remaining lines.
The UHSIF library provides a set of default mappings, as shown in Table 3-2. For other mappings, please contact
technical support.
Table 3-2 Pin default mapping configuration
UHSIF_PORT Pin function UHSIF_PORT Pin function UHSIF_PORT Pin function
UHSIF_PORT0 NC UHSIF_PORT16 DATA[0] UHSIF_PORT32 DATA[16]
UHSIF_PORT1 NC UHSIF_PORT17 DATA[1] UHSIF_PORT33 DATA[17]
UHSIF_PORT2 NC UHSIF_PORT18 DATA[2] UHSIF_PORT34 DATA[18]
UHSIF_PORT3 SEL[0] UHSIF_PORT19 DATA[3] UHSIF_PORT35 DATA[19]
UHSIF_PORT4 SEL[1] UHSIF_PORT20 DATA[4] UHSIF_PORT36 DATA[20]
UHSIF_PORT5 AF# UHSIF_PORT21 DATA[5] UHSIF_PORT37 DATA[21]
UHSIF_PORT6 NC UHSIF_PORT22 DATA[6] UHSIF_PORT38 DATA[22]
UHSIF_PORT7 AE# UHSIF_PORT23 DATA[7] UHSIF_PORT39 DATA[23]
UHSIF_PORT8 EOP# UHSIF_PORT24 DATA[8] UHSIF_PORT40 DATA[24]
UHSIF_PORT9 WRNF UHSIF_PORT25 DATA[9] UHSIF_PORT41 DATA[25]
UHSIF_PORT10 NC UHSIF_PORT26 DATA[10] UHSIF_PORT42 DATA[26]
UHSIF_PORT11 RDNE UHSIF_PORT27 DATA[11] UHSIF_PORT43 DATA[27]
UHSIF_PORT12 RD# UHSIF_PORT28 DATA[12] UHSIF_PORT44 DATA[28]
UHSIF_PORT13 OE# UHSIF_PORT29 DATA[13] UHSIF_PORT45 DATA[29]
UHSIF_PORT14 WR# UHSIF_PORT30 DATA[14] UHSIF_PORT46 DATA[30]
UHSIF_PORT15 CS# UHSIF_PORT31 DATA[15] UHSIF_PORT47 DATA[31]
The mapping of UHSIF peripheral signals to MCU I/O ports can be configured via the UHSIF_PORT_RM
register. For details, refer to the "UHSIF Pin Functions" section in the CH32H417DS0.PDF.
V1.0 2

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
4. Functional Description
4.1. Transmission Lines and Buffers
Figure 4-1 UHSIF transmission line and buffer
Buffer 0
Line 0 ...
Buffer 7
Buffer 0
Line 1 ...
Buffer 7
Data
Buffer 0
Line 2 ...
Buffer 7
Buffer 0
Line 3 ...
Buffer 7
UHSIF
Transmission lines (Lines) are the 4 data channels used for high-speed data transfer within the UHSIF. They are
selected via the external address lines SEL[1:0]. When the address lines switch, the transmission lines can switch
without delay to continue data transmission and reception.
Each transmission line contains 8 buffers. By configuring these buffers, the UHSIF can implement up to 32
independent data paths. Each transmission line can notify the CPU of the status of its internal buffers via
interrupts.
4.2. Communication Timing Description
4.2.1. Master Write Slave
When the UHSIF master writes data to the slave, it is divided into 2 processes: writing non-zero length packets
and zero length packets.
 The master writes non-zero length packets to the slave
Figure 4-2 Timing of master writing non-zero length packet to slave
PCLK
CS#
tIS
WR# t(WEN2FLAG) t(WEN2FLAG)
EOP#
DATA WDATA WDATA WDATA WDATA WDATA WDATA
SEL[1:0] SEL1 SEL0 SEL1 SEL0
WRNF
t(W_WM)
AF#
When the WRNF signal is valid, the UHSIF master can initiate a data write operation to the slave. According to
the length of data written by the master, it can be divided into the following 2 situations:
V1.0 3

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
1. When the length of data sent by the master is less than or equal to the length of data buffer received by the
slave:
(1) The master drives the SEL1 and SEL0 signals to select the appropriate transmission line;
(2) The master drives the CS# and WR# signals and sends data to the data bus;
(3) After writing the data, the master drives the WR# signal to a high level; the slave invalidates the WRNF signal
after 2 clock cycles.
2. When the length of data sent by the master is greater than the length of data buffer received by the slave:
(1) The master drives the SEL1 and SEL0 signals to select the appropriate transmission line;
(2) The master drives the CS# and WR# signals and sends data to the data bus;
(3) When the slave detects that the receive buffer is about to become full, it drives the AF# signal to a low level to
notify the master. The master then sets WR# to a high level based on the watermark value to complete the write
process, and the slave sets WRNF to an invalid state after 2 clock cycles.
 Zero-length packet
Figure 4-3 Timing of master writing zero-length packets to slave
PCLK
CS#
WR#
EOP#
t(WEN2FLAG)
DATA
SEL[1:0] SELx
WRNF
1. The host drives the SEL1 and SEL0 signals to select the appropriate transmission line (Line);
2. The host pulls the EOP# and CS# signals low to indicate that the current transmission is a zero-length packet;
3. After transmission is complete, the host pulls the EOP# and CS# signals high.
4.2.2. Master Read Slave
Figure 4-4 Timing of master reading zero-length packets to slave
PCLK
CS#
RD#
t(RDN2FLAG)
OE#
t(RDN2DATV) t(RDN2DATV)
t(RDN2FLAG)
DATA RDATA RDATA RDATA RDATA RDATA RDATA
SEL[1:0] SEL0
RDNE
t(R_WM)
AE#
When RDNE is active, the master can initiate a data read. Depending on the length of data the master can receive,
there are 2 scenarios:
1. When the length of data the master can receive is less than or equal to the length of data sent by the slave:
V1.0 4

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
a The master drives the SEL1 and SEL0 signals to select the appropriate data line;
b The master drives the OE# and CS# signals, and the data bus is then controlled by the slave;
c The master drives RD#, and the slave returns data to the master after 2 clock cycles;
d After reading the data, the master sets RD#, CS#, and OE# to high, ending the read process; the slave sets
RDNE to invalid 2 clock cycles after the RD# high level expires.
2. When the length of data the master can receive is greater than the length of data sent by the slave:
a The master drives the SEL1 and SEL0 signals to select the appropriate data line;
b The master pulls the OE# and CS# signals low, handing control of the data bus over to the slave;
c The master sets RD# to a low level; the slave returns data to the host after two clock cycles;
d When the slave detects that the host is about to finish reading the transmit buffer, it sets AE# to a low level to
notify the master. The master then sets RD#, CS#, and OE# to high levels based on the watermark value,
complete the read process. The slave sets RDNE to an invalid state 2 clock cycles after the RD# high level
expires.
Table 4-2 Master read/write slave parameters
Parameter Description Fixed value Unit
The time from when the WR#/EOP# signal is pulled high until
t 2 cycle
(WEN2FLAG)
the WRNF signal going low when write slave is completed
The time at which the AF# is lowered in advance when the
t (1) cycle
(W_WM)
buffer is about to fill up
The time from when the RD# signal is pulled low until valid
t 2 cycle
(RDN2DATV)
data appears on the data bus when read slave
The time from when the RD# signal is pulled high until slave
t 2 cycle
(RDN2FLAG)
RDNE going low when read slave is completed
The time at which AE# is lowered in advance when the buffer is
t (1) cycle
(R_WM)
about to run out
Note: 1. Defined by the "water_mark_value" parameter in the UHSIF_Line_Cfg API.
V1.0 5

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
5. UHSIF Library Function Description
5.1. Host Configuration Process
1. Use UHSIF_GPIO_Init to configure the host mode, pin mapping, clock frequency, and data bus width;
UHSIF_GPIO_Init( DEF_UHSIF_MASTER_MODE,
DEF_UHSIF_PINREMAP2,
DEF_UHSIF_CLKREMAP1,
RCC_UHSIFDIV_DIV4,
DEF_UHSIF_DATA_BIT32 );
2. Configure related registers;
UHSIF_Cfg( );
3. Configure the transmission line, the number of buffers, the send and receive buffer addresses, and the
watermark value;
UHSIF_Line_Cfg( DEF_LINE0,
DEF_LINE_DIR_IN,
DEF_BUFF_COUNT_8,
USBSS_EP1_Tx_Buf,
0 );
UHSIF_Line_Cfg( DEF_LINE1,
DEF_LINE_DIR_OUT,
DEF_BUFF_COUNT_8,
USBSS_EP1_Rx_Buf,
0 );
4. Start the transmission; by default, the system will receive one packet of data after the transmission begins;
UHSIF_Start( ENABLE );
5. To continue sending or receiving data, use the UHSIF_Trans_Cfg function. In this function, DEF_LINE0
enables data reception on transmission line 0 until the UHSIF_RD_COMM.dealth buffer is received; when
receiving data, simply set the trans_size parameter to 0.
UHSIF_Trans_Cfg( DEF_LINE0, UHSIF_RD_COMM.deal, 0 );
5.2. Slave Configuration Process
1. Use UHSIF_GPIO_Init to configure the slave mode, pin mapping, clock frequency, and data bus width. Select
either FPGA mode or SOC mode for the slave mode depending on your application;
V1.0 6

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
UHSIF_GPIO_Init( DEF_UHSIF_SLAVE_SOC_MODE,
DEF_UHSIF_PINREMAP2,
DEF_UHSIF_CLKREMAP1,
0,
DEF_UHSIF_DATA_BIT32 );
2. Configure related registers;
UHSIF_Cfg();
3. Configure the transmission line, the number of buffers, the send and receive buffer addresses, and the
watermark value;
UHSIF_Line_Cfg( DEF_LINE0,
DEF_LINE_DIR_IN,
DEF_BUFF_COUNT_8,
USBSS_EP1_Tx_Buf,
4094 );
UHSIF_Line_Cfg( DEF_LINE1,
DEF_LINE_DIR_OUT,
DEF_BUFF_COUNT_8,
USBSS_EP1_Rx_Buf,
4 );
4. Start the transmission; by default, the system will receive one packet of data after the transmission begins;
UHSIF_Start( ENABLE );
5. To continue sending or receiving data, use the UHSIF_Trans_Cfg function, where DEF_LINE0 enables data
reception on transmission line 0. This will receive data until the UHSIF_RD_COMM.dealth buffer is reached;
when receiving, simply set the trans_size parameter to 0.
UHSIF_Trans_Cfg( DEF_LINE0, UHSIF_RD_COMM.deal, 0 );
5.3. API Description
5.3.1. UHSIF_Get_Ver
Get the current UHSIF library version number.
Interface definition:
uint8_t UHSIF_Get_Ver( void );
Parameter Description
Return Current UHSIF library version number
V1.0 7

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
5.3.2. UHSIF_Cfg
Initialize the UHSIF registers. This function must be called after the UHSIF GPIO has been initialized and before
the transmission lines are initialized.
Interface definition:
void UHSIF_Cfg( void );
Parameter Description
None Initialize UHSIF related registers
5.3.3. UHSIF_GPIO_Init
UHSIF pin initialization is used to configure master and slave modes, as well as to configure pin remapping.
UHSIF modes include slave FPGA mode, slave SOC mode, and host mode. When the master is an FPGA, the
slave must use FPGA mode; the slave SOC mode is only applicable when connecting to a host of the same type.
The maximum clock frequency for UHSIF is 125MHz, derived from the SYSCLK clock. When UHSIF is in
master mode, the clock division factor can be configured via clk_div.
Interface Definition:
uint8_t UHSIF_GPIO_Init( uint8_t mode_select,
uint8_t uhsif_port_rm,
uint8_t uhsif_clk_rmm,
uint8_t clk_div,
uint8_t width_bit );
Parameter Description
mode_select Select to configure master mode or slave mode.
Select the remapping pin of UHSIF control line and data
uhsif_port_rm
line.
uhsif_clk_rmm Select the remap pin of the UHSIF clock line.
clk_div Clock frequency division coefficient in UHSIF master mode
width_bit Select the data bus width as 8/16/24/32-bit.
Return Whether Pin initialization is successful
5.3.4. UHSIF_Line_Cfg
UHSIF transmission line initialization is used to configure the transmission line number, transmission direction,
number of buffers used by the transmission line, and the addresses of the send and receive buffers for the current
transmission line.
Since UHSIF has a total of 4 transmission lines, the line_num value can range from 0 to 3;
This function allows for the configuration of multiple transmission lines for data transmission and reception;
however, each transmission line can only be configured for a single direction.
Each transmission line supports up to 8 buffers, so buff_count can be set to a value between 1 and 8.
water_mark_value specifies the number of cycles in advance by which the signal should be pulled low upon
completion of transmission. For example, if DEF_BUFF_SIZE is set to 16K and you want to pull the signal low 2
cycles in advance, the value of water_mark_value is 16384/16 – 2 = 4094.
V1.0 8

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
Interface Definition:
uint8_t UHSIF_Line_Cfg( uint8_t line_num,
uint8_t line_dir,
uint8_t buff_count,
uint8_t *pbuf,
uint16_t water_mark_value);
Parameter Description
line_num Select the transmission line number to initialize
line_dir Current transmission line direction configuration
buff_count Current transmission line BUFF number configuration
Address of buffer used to transmit and receive data on
*pbuf
current transmission line
Indicates the number of words remaining to be transmitted
water_mark_value in the buffer when transmitted and the number of words to
be received in the buffer when received
Return Whether transmission line configuration is successful
5.3.5. UHSIF_Start
UHISF activated. After the function is configured, the first buff of the configured receiving transmission line
enables data reception once.
Interface definition:
void UHSIF_Start( FunctionalState sta );
Parameter Description
sta Select whether to enable parallel port function
5.3.6. UHSIF_Linex_IN_Callback
The UHISF transmission line receives an interrupt callback function; this interrupt is triggered when the
transmission line receives a long or short packet. The 'rcv_count' value read represents the length of the data
received during this transmission.
Interface definition:
void UHSIF_Linex_IN_Callback( uint32_t rcv_count );
Parameter Description
rcv_count Length of data received on the current transmission line
5.3.7. UHSIF_Linex_OUT_Callback
The UHISF transmission line sends an interrupt callback function; this interrupt function is called once the
transmission line has finished sending data.
Interface definition:
void UHSIF_Linex_OUT_Callback( void );
V1.0 9

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
Parameter Description
None UHSIF transmission line send interrupt callback function
5.3.8. UHSIF_Trans_Cfg
Enable a single UHSIF data transmission or reception.
Since UHSIF has a total of 4 transmission lines, the line_num value can be set to 0–3;
Based on the buff_count value configured via the UHSIF_Line_Cfg function, buff_cur can be set to any value
between 0 and buff_count – 1; it is incremented and reused in a loop during operation;
When configuring a transmission line to send data, the trans_size value represents the length of the data to be sent;
when configuring a transmission line to receive data, this value is irrelevant and should be set to 0.
Interface definition:
uint8_t UHSIF_Trans_Cfg( uint8_t line_num,
uint8_t buff_cur,
uint32_t trans_size );
Parameter Description
line_num Select the transmission line number to use
buff_cur Select the number of buffs to use for this transmission line
trans_size Configure the length of data sent this time
Return Whether the configuration parameter is valid
5.3.9. UHSIF_Reg_Change
The UHSIF has a total of 76 registers that can be modified; the offset address reg_addr ranges from 0 to 75, and
value should be set to the value you wish to modify.
uit8_t UHSIF_ Reg _Cfg( uint8_t mode,
uint8_t reg_addr,
uint32_t value );
Parameter Description
mode Master/Slave register select
reg_addr Register address
value Register value to be modified
Return whether the operation is successful
V1.0 10

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
6. Introduction to Evaluation Board
CH32H417 UHSIF offers a variety of evaluation boards for use with this product.
6.1. CH32H417MEU6-UHSIF-Bottom-R0-1v0
CH32H417MEU6 UHSIF Evaluation Board base board, featuring an on-board debug interface, USB3.0 port,
external Flash, and UHSIF interface. It is compatible with multiple evaluation board top plates.
Figure 6-1 CH32H417MEU6-UHSIF-Bottom-R0-1v0 evaluation board
6.2. CH32H417MEU6-UHSIF-Top-R0-1v0
CH32H417MEU6 UHSIF Evaluation Board Top Panel, featuring an on-board debug interface, USB3.0 port,
external Flash, and UHSIF interface. Must be used in conjunction with the CH32H417MEU6-UHSIF-Bottom-R0.
Suitable for demonstrating UHSIF-related examples.
Figure 6-2 CH32H417MEU6-UHSIF-Top-R0-1v0 evaluation board
6.3. FPGA-UHSIF-Top-R0-1v0
UHSIF-compatible FPGA evaluation board, designed for use with the CH32H417MEU6-UHSIF-Bottom-R0.
It can be used to demonstrate UHSIF-related examples.
V1.0 11

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
Figure 6-3 FPGA-UHSIF-Top-R0-1v0 evaluation board
V1.0 12

CH32H417 UHSIF Development Reference Manual https://wch-ic.com
7. Electrical Characteristics
SLAVE_IN(1)
t IS t IH t CK
PCLK
t
OD
SLAVE_OUT(1)
Note: 1. SLAVE_IN refers to the slave input, and SLAVE_OUT refers to the slave output.
Table 4-2 Slave electrical parameters
Symbol Parameter description Condition Min. Max. Unit
f /t Clock frequency in data transmission mode CL≤10pF, V = 1.8V 125 MHz
CK CK DD18
t Clock cycle 8 ns
C
t Settling time from the input signal to CLK 0.5 ns
IS
Holding time from slave input signal to
t 1.5 ns
IH
CLK
t Delay from slave output signal to CLK 6.2 8 ns
OD
V1.0 13
