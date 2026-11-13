SN74CBTLV3257
SCDS040N – DECEMBER 1997 – REVISED JULY 2026
SN74CBTLV3257 Low-Voltage 4-Bit 1-of-2 FET Multiplexer/Demultiplexer
1 Features 3 Description
• 5Ω Switch Connection Between Two Ports The SN74CBTLV3257 device is a 1-of-8 high-speed
• Rail-to-Rail Switching on Data I/O Ports FET  multiplexer/demultiplexer.  The  low  on-state
• I  Supports Partial-Power-Down Mode Operation resistance  of  the  switch  allows  connections  to  be
off
• Latch-Up Performance Exceeds 100mA Per JESD  made  with  minimal  propagation  delay.  The  select
78, Class II inputs  (S0,  S1,  S2)  control  the  data  flow.  The
• ESD Protection Exceeds JESD 22 FET  multiplexers/demultiplexers  are  disabled  when
– 2000V Human-Body Model (A114-A) the output-enable ( OE) input is high. This device
is fully specified for partial-power-down applications
– 200V Machine Model (A115-A)
| using  Ioff.  | The  Ioff  | feature  | ensures  | that  damaging  |
| ------------- | ---------- | -------- | -------- | --------------- |
2 Applications
current cannot backflow through the device when it is
powered down. The device has isolation during power
• Datacenter and enterprise computing
off. To ensure the high-impedance state during power
• Broadband fixed line access
up or power down, OE must be tied to VCC through
• Building automation
• Wired networking a pullup resistor; the minimum value of the resistor
is determined by the current-sinking capability of the
• Motor drives
driver.
Package Information
| PART NUMBER       |     | PACKAGE (1)    |     | PACKAGE SIZE(2) |
| ----------------- | --- | -------------- | --- | --------------- |
| SN74CBTLV3257DBQR |     | DBQ (SSOP, 16) |     | 4.90mm × 3.90mm |
| SN74CBTLV3257PWR  |     | PW (TSSOP, 16) |     | 5.00mm × 4.40mm |
| SN74CBTLV3257DGVR |     | DGV(TVSOP,16)  |     | 3.60mm × 4.40mm |
| SN74CBTLV3257DR   |     | D (SOIC, 16)   |     | 9.90mm × 3.91mm |
| SN74CBTLV3257RGYR |     | RGY (VQFN, 16) |     | 4.00mm × 3.50mm |
| SN74CBTLV3257DYY  |     | SOT (16)       |     | 4.20mm × 2.00mm |
| SN74CBTLV3257BQB  |     | WQFN (16)      |     | 3.50mm × 2.50mm |
(1) For more information, see Section 11.
(2) The package size (length × width) is a nominal value and
includes pins, where applicable.
Simplified Schematic (Each FET Switch)
An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.

SN74CBTLV3257
SCDS040N – DECEMBER 1997 – REVISED JULY 2026 www.ti.com
Table of Contents
1 Features............................................................................1 7.1 Overview...................................................................10
2 Applications.....................................................................1 7.2 Functional Block Diagram.........................................10
3 Description.......................................................................1 7.3 Feature Description...................................................10
4 Pin Configuration and Functions...................................3 7.4 Device Functional Modes..........................................10
5 Specifications..................................................................5 8 Application and Implementation..................................11
5.1 Absolute Maximum Ratings........................................5 8.1 Application Information..............................................11
5.2 ESD Ratings...............................................................5 8.2 Typical Application....................................................11
5.3 Thermal Information....................................................5 8.3 Power Supply Recommendations.............................12
5.4 Recommended Operating Conditions.........................6 8.4 Layout.......................................................................13
5.5 Electrical Characteristics - DBQ, DGV, D, PW 9 Device and Documentation Support............................14
and RGY only................................................................6 9.1 Documentation Support............................................14
5.6 Electrical Characteristics - DYY and BQB 9.2 Receiving Notification of Documentation Updates....14
Package only.................................................................7 9.3 Support Resources...................................................14
5.7 Switching Characteristics - DBQ, DGV, D, PW 9.4 Trademarks...............................................................14
and RGY only................................................................7 9.5 Electrostatic Discharge Caution................................14
5.8 Switching Characteristics - DYY and BQB 9.6 Glossary....................................................................14
Package only.................................................................8 10 Revision History..........................................................15
5.9 Typical Characteristics................................................8 11 Mechanical, Packaging, and Orderable
6 Parameter Measurement Information............................9 Information....................................................................15
7 Detailed Description......................................................10
2 Submit Document Feedback Copyright © 2026 Texas Instruments Incorporated
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
| www.ti.com |     |     |     | SCDS040N – DECEMBER 1997 – REVISED JULY 2026 |     |
| ---------- | --- | --- | --- | -------------------------------------------- | --- |
4 Pin Configuration and Functions
 CCV
   S
| S 1   | 16  |  VCC  |     |         |        |
| ----- | --- | ----- | --- | ------- | ------ |
| 1B1 2 | 15  |  OE   |     |         |        |
|       |     |       |     | 1       | 61     |
| 1B2 3 | 14  |  4B1  |     |         |        |
|       |     |       | 1B1 | 2       | 15 OE  |
| 1A 4  | 13  |  4B2  |     |         |        |
|       |     |       | 1B2 | 3       | 14 4B1 |
| 2B1 5 | 12  |  4A   |     | Thermal |        |
|       |     |       | 1A  | 4       | 13 4B2 |
Pad
| 2B2 6 | 11  |  3B1 | 2B1 | 5   | 12 4A  |
| ----- | --- | ---- | --- | --- | ------ |
| 2A 7  | 10  |  3B2 |     |     |        |
|       |     |      | 2B2 | 6   | 11 3B1 |
| GND 8 | 9   |  3A  |     |     |        |
|       |     |      | 2A  | 7   | 10 3B2 |
|       |     |      |     | 8   | 9      |
Not to scale
Figure 4-1. DGV, D, DBQ, DYY, and PW Package 16-
Not to scale
| Pin TVSOP, SOIC, SSOP, SOT-23-THIN, and TSSOP  |     |     |     | DNG | A3  |
| ---------------------------------------------- | --- | --- | --- | --- | --- |
(Top View)
Figure 4-2. RGY, and BQB Package 16-Pin VQFN,
and WQFN (Top View)
 CCV
1B1
EO
S
|     | 61  | 51 41 | 31  |     |     |
| --- | --- | ----- | --- | --- | --- |
|     | 1B2 | 1 12  | 4B1 |     |     |
|     | 1A  | 2 11  | 4B2 |     |     |
|     | 2B1 | 3 10  | 4A  |     |     |
|     | 2B2 | 4 9   | 3B1 |     |     |
|     | 5   | 6 7   | 8   |     |     |
Not to scale
|     | A2  | DNG A3 | 2B3 |     |     |
| --- | --- | ------ | --- | --- | --- |
Copyright © 2026 Texas Instruments Incorporated Submit Document Feedback 3
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
SCDS040N – DECEMBER 1997 – REVISED JULY 2026 www.ti.com
Table 4-1. Pin Functions
PIN
TYPE DESCRIPTION
| NAME | NO  |                             |
| ---- | --- | --------------------------- |
| 1A   | 4   | I/O Channel 1 out/in common |
| 1B1  | 2   | I/O Channel 1 in/out 1      |
| 1B2  | 3   | I/O Channel 1 in/out 2      |
| 2A   | 7   | I/O Channel 2 out/in common |
| 2B1  | 5   | I/O Channel 2 in/out 1      |
| 2B2  | 6   | I/O Channel 2 in/out 2      |
| 3A   | 9   | I/O Channel 3 out/in common |
| 3B1  | 11  | I/O Channel 3 in/out 1      |
| 3B2  | 10  | I/O Channel 3 in/out 2      |
| 4A   | 12  | I/O Channel 4 out/in common |
| 4B1  | 14  | I/O Channel 4 in/out 1      |
| 4B2  | 13  | I/O Channel 4 in/out 2      |
| GND  | 8   | — Ground                    |
| OE   | 15  | I Output Enable, active low |
| S    | 1   | I Select                    |
| V CC | 16  | — Power                     |
Table 4-2. UQFN Pin Functions
PIN
I/O DESCRIPTION
| NAME | NO. |                             |
| ---- | --- | --------------------------- |
| 1A   | 2   | I/O Channel 1 out/in common |
| 1B1  | 16  | I/O Channel 1 in/out 1      |
| 1B2  | 1   | I/O Channel 1 in/out 2      |
| 2A   | 5   | I/O Channel 2 out/in common |
| 2B1  | 3   | I/O Channel 2 in/out 1      |
| 2B2  | 4   | I/O Channel 2 in/out 2      |
| 3A   | 7   | I/O Channel 3 out/in common |
| 3B1  | 9   | I/O Channel 3 in/out 1      |
| 3B2  | 8   | I/O Channel 3 in/out 2      |
| 4A   | 10  | I/O Channel 4 out/in common |
| 4B1  | 12  | I/O Channel 4 in/out 1      |
| 4B2  | 11  | I/O Channel 4 in/out 2      |
| GND  | 6   | — Ground                    |
| OE   | 13  | I Output Enable, active low |
| S    | 15  | I Select                    |
| V    | 14  | — Power                     |
CC
4 Submit Document Feedback Copyright © 2026 Texas Instruments Incorporated
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
| www.ti.com |     |     |     | SCDS040N – DECEMBER 1997 – REVISED JULY 2026 |     |     |
| ---------- | --- | --- | --- | -------------------------------------------- | --- | --- |
5 Specifications
5.1 Absolute Maximum Ratings
over operating free-air temperature range (unless otherwise noted)(1)
|                  |     |     |     | MIN  | MAX | UNIT |
| ---------------- | --- | --- | --- | ---- | --- | ---- |
| V Supply voltage |     |     |     | –0.5 | 4.6 | V    |
CC
| V Input voltage(2) |     |     |     | –0.5 | 4.6 | V   |
| ------------------ | --- | --- | --- | ---- | --- | --- |
I
| Continuous channel current |     |        |     |     | 128 | mA  |
| -------------------------- | --- | ------ | --- | --- | --- | --- |
| I Input clamp current      |     | V  < 0 |     |     | –50 | mA  |
| IK                         |     | I/O    |     |     |     |     |
| T J Junction temperature   |     |        |     |     | 150 | °C  |
| T Storage temperature      |     |        |     | –65 | 150 | °C  |
stg
(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply
functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions.
If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully
functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.
(2) The input and output negative-voltage ratings may be exceeded if the input and output clamp-current ratings are observed.
5.2 ESD Ratings
|     |     |     |     |     | VALUE | UNIT |
| --- | --- | --- | --- | --- | ----- | ---- |
V (ESD) Electrostatic discharge Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1) 2000 V
(1) JEDEC document JEP155 states that 500V HBM allows safe manufacturing with a standard ESD control process.
5.3 Thermal Information
SN74CBTLV3257
DGV
|     |                   | D DBQ           | PW          | RGY             | BQB     |      |
| --- | ----------------- | --------------- | ----------- | --------------- | ------- | ---- |
|     |                   |                 | (TVSO       | DYY (SOT)       |         |      |
|     | THERMAL METRIC(1) | (SOIC) (SSOP)   | (TSSOP)     | (VQFN)          |         | UNIT |
|     |                   |                 | P)          |                 | (WQFN)  |      |
|     |                   | 16 PINS 16 PINS | 16  16 PINS | 16 PINS 16 PINS | 16 PINS |      |
PINS
R Junction-to-ambient thermal resistance 102.5 116.6 123.1 129.1 78.4 129.9 88.1 °C/W
θJA
R
θ Junction-to-case (top) thermal resistance 65.4 70 48.7 67 52.5 78.4 58.3 °C/W
JC(top)
R Junction-to-board thermal resistance 65.2 75 54.9 87.1 21.74 73.3 17.0 °C/W
θJB
ψ Junction-to-top characterization parameter 25.5 17 5.2 14.5 52.5 17.2 58.3 °C/W
JT
ψ JB Junction-to-board characterization parameter 64.6 74.1 54.3 86.3 76.6 72.4 85.1 °C/W
R θ
Junction-to-case (bottom) thermal resistance n/a n/a n/a n/a 37.3 n/a 37.5 °C/W
JC(bot)
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
note.
Copyright © 2026 Texas Instruments Incorporated Submit Document Feedback 5
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
| SCDS040N – DECEMBER 1997 – REVISED JULY 2026 |     |     |     |     |     |     | www.ti.com |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- |
5.4 Recommended Operating Conditions
over operating free-air temperature range (unless otherwise noted)(1)
|                  |     |     |     |     |     | MIN | MAX UNIT |
| ---------------- | --- | --- | --- | --- | --- | --- | -------- |
| V Supply voltage |     |     |     |     |     | 2.3 | 3.6 V    |
CC
|                                    |     |     | V CC  = 2.3V to 2.7V |     |     | 1.7 |     |
| ---------------------------------- | --- | --- | -------------------- | --- | --- | --- | --- |
| V High-level control input voltage |     |     |                      |     |     |     | V   |
IH
|     |     |     | V CC  = 2.7V to 3.6V |     |     | 2   |     |
| --- | --- | --- | -------------------- | --- | --- | --- | --- |
|     |     |     | V  = 2.3V to 2.7V    |     |     |     | 0.7 |
CC
| V IL Low-level control input voltage |     |     |                   |     |     |     | V   |
| ------------------------------------ | --- | --- | ----------------- | --- | --- | --- | --- |
|                                      |     |     | V  = 2.7V to 3.6V |     |     |     | 0.8 |
CC
T Operating free-air temperature PKG = RGY, DBQ, D, PW, DGV –40 85 °C
A
| T A Operating free-air temperature |     |     | PKG = DYY, BQB |     |     | –40 | 125 °C |
| ---------------------------------- | --- | --- | -------------- | --- | --- | --- | ------ |
(1) All unused control inputs of the device must be held at V CC  or GND to ensure proper device operation. See Implications of Slow or
Floating CMOS Inputs.
5.5 Electrical Characteristics - DBQ, DGV, D, PW and RGY only
over recommended operating free-air temperature range T  = -40 to 85°C (unless otherwise noted)
A
| PARAMETER      |               |     | TEST CONDITIONS     |                   | MIN | TYP(1) | MAX UNIT |
| -------------- | ------------- | --- | ------------------- | ----------------- | --- | ------ | -------- |
| V              | V  = 3V,      |     | I = –18mA           |                   |     |        | –1.2 V   |
| IK             | CC            |     | I                   |                   |     |        |          |
| I              | V  = 3.6V,    |     | V = V  or GND       |                   |     |        | ±1 µA    |
| I              | CC            |     | I CC                |                   |     |        |          |
| I              | V  = 0,       |     | V or V  = 0 to 3.6V |                   |     |        | 15 µA    |
| off            | CC            |     | I O                 |                   |     |        |          |
| I              | V  = 3.6V,    |     | I  = 0,             | V = V  or GND     |     |        | 10 µA    |
| CC             | CC            |     | O                   | I CC              |     |        |          |
|  (2)           |               |     |                     | Other inputs at V | CC  |        |          |
| ∆I CC Control  | V CC  = 3.6V, |     | One input at 3V,    |                   |     |        | 300 µA   |
or GND
inputs
| C              | V = 3V or 0   |     |        |          |     |      | 3 pF |
| -------------- | ------------- | --- | ------ | -------- | --- | ---- | ---- |
| i              | I             |     |        |          |     |      |      |
| A port         |               |     |        |          |     | 10.5 |      |
| C              | V  = 3V or 0, |     | OE = V |          |     |      | pF   |
| io(OFF) B port | O             |     | CC     |          |     | 5.5  |      |
|                |               |     |        | I = 64mA |     |      | 5 8  |
I
|     | V  = 2.3V, |         | V I  = 0 |          |     |     |     |
| --- | ---------- | ------- | -------- | -------- | --- | --- | --- |
|     | CC         |         |          | I = 24mA |     |     | 5 8 |
|     | TYP at V   |  = 2.5V |          | I        |     |     |     |
CC
|        |     |     | V = 1.7V | I = 15mA |     | 27  | 40  |
| ------ | --- | --- | -------- | -------- | --- | --- | --- |
| r  (3) |     |     | I        | I        |     |     | Ω   |
on
|     |     |     |     | I = 64mA I |     |     | 5 7 |
| --- | --- | --- | --- | ---------- | --- | --- | --- |
V = 0
|                                 | V  = 3V |                                     | I        | I = 24mA |     |     | 5 7 |
| ------------------------------- | ------- | ----------------------------------- | -------- | -------- | --- | --- | --- |
|                                 | CC      |                                     |          | I        |     |     |     |
|                                 |         |                                     | V = 2.4V | I = 15mA |     | 10  | 15  |
|                                 |         |                                     | I        | I        |     |     |     |
| (1) All typical values are at V |         |  = 3.3V (unless otherwise noted), T |          |  = 25°C. |     |     |     |
|                                 |         | CC                                  |          | A        |     |     |     |
(2) This is the increase in supply current for each input that is at the specified voltage level, rather than V  or GND.
CC
(3) Measured by the voltage drop between the A and the B terminals at the indicated current through the switch. On-state resistance is
determined by the lower of the voltages of the two (A or B) terminals.
6 Submit Document Feedback Copyright © 2026 Texas Instruments Incorporated
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
| www.ti.com |     |     |     |     |     |     | SCDS040N – DECEMBER 1997 – REVISED JULY 2026 |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
5.6 Electrical Characteristics - DYY and BQB Package only
over recommended operating free-air temperature range T  = -40 to 125°C (PKG = DYY, BQB) (unless otherwise noted)
A
| PARAMETER |      |          | TEST CONDITIONS |                  |     |       |         | MIN | TYP(1) | MAX  | UNIT |
| --------- | ---- | -------- | --------------- | ---------------- | --- | ----- | ------- | --- | ------ | ---- | ---- |
| V IK      | V CC |  = 3V,   | I = –18mA       | I                |     |       |         |     |        | -1.2 | V    |
| I I       | V CC |  = 3.6V, | V = V           | I CC  or GND     |     |       |         |     |        | ±1   | µA   |
| I off     | V CC |  = 0,    | V or V          | I O  = 0 to 3.6V |     |       |         |     |        | 15   | µA   |
| I         | V    |  = 3.6V, | I               |  = 0,            |     | V = V |  or GND |     |        | 10   | µA   |
| CC        | CC   |          |                 | O                |     | I CC  |         |     |        |      |      |
Other inputs at V
| ∆I  (2) Control  | V   |  = 3.6V, | One input at 3V, |     |     |        | CC  |     |     | 300 | µA  |
| ---------------- | --- | -------- | ---------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
| CC               | CC  |          |                  |     |     | or GND |     |     |     |     |     |
inputs
| C i     | V = 3V or 0 I |     |        |     |     |          |     |     |      | 3    | pF  |
| ------- | ------------- | --- | ------ | --- | --- | -------- | --- | --- | ---- | ---- | --- |
| A port  |               |     |        |     |     |          |     |     | 10.5 |      |     |
| C       | V  = 3V or 0, |     | OE = V |     |     |          |     |     |      |      | pF  |
| io(OFF) | O             |     |        | CC  |     |          |     |     |      |      |     |
| B port  |               |     |        |     |     |          |     |     |      | 6    |     |
|         |               |     |        |     |     | I = 64mA |     |     |      | 5 10 |     |
I
V = 0
|      | V CC     |  = 2.3V,   |          | I   |     |            |     |     |     |      |     |
| ---- | -------- | ---------- | -------- | --- | --- | ---------- | --- | --- | --- | ---- | --- |
|      |          |            |          |     |     | I = 24mA I |     |     |     | 5 10 |     |
|      | TYP at V | CC  = 2.5V |          |     |     |            |     |     |     |      |     |
|      |          |            | V = 1.7V |     |     | I = 15mA   |     |     | 27  | 40   |     |
|  (3) |          |            |          | I   |     | I          |     |     |     |      |     |
| r on |          |            |          |     |     |            |     |     |     |      | Ω   |
|      |          |            |          |     |     | I = 64mA   |     |     |     | 5    | 9   |
I
V = 0 I
|                                 | V   |  = 3V                                  |          |     |            | I = 24mA   |     |     |     | 5   | 9   |
| ------------------------------- | --- | -------------------------------------- | -------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- |
|                                 | CC  |                                        |          |     |            | I          |     |     |     |     |     |
|                                 |     |                                        | V = 2.4V | I   |            | I = 15mA I |     |     | 10  | 20  |     |
| (1) All typical values are at V |     | CC  = 3.3V (unless otherwise noted), T |          |     | A  = 25°C. |            |     |     |     |     |     |
(2) This is the increase in supply current for each input that is at the specified voltage level, rather than V CC  or GND.
(3) Measured by the voltage drop between the A and the B terminals at the indicated current through the switch. On-state resistance is
determined by the lower of the voltages of the two (A or B) terminals.
5.7 Switching Characteristics - DBQ, DGV, D, PW and RGY only
over recommended operating free-air temperature range -40 to 85°C (unless otherwise noted) (See Figure 6-1)
|           |     |              |     |             |        |     | V  = 2.5 ± 0.2V | V    |  = 3.3V ± 0.3V |      |      |
| --------- | --- | ------------ | --- | ----------- | ------ | --- | --------------- | ---- | -------------- | ---- | ---- |
|           |     |              |     |             |        |     | CC              |      | CC             |      |      |
| PARAMETER |     | FROM (INPUT) |     | TO (OUTPUT) |        |     |                 |      |                |      | UNIT |
|           |     |              |     |             |        |     | MIN             | MAX  | MIN            | MAX  |      |
|           |     | A or B(1)    |     |             | B or A |     |                 | 0.15 |                | 0.25 |      |
| t         |     |              |     |             |        |     |                 |      |                |      | ns   |
pd
|      |     | S   |     |     | A   |     | 1.8 | 6.1 | 1.8 | 5.3 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t en |     | S   |     |     | B   |     | 1.7 | 6.1 | 1.7 | 5.3 | ns  |
| t    |     | S   |     |     | B   |     | 1   | 4.8 | 1   | 4.5 | ns  |
dis
| t   |     | OE  |     |     | A or B |     | 1.9 | 5.6 | 2   |     | 5 ns |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | ---- |
en
| t   |     | OE  |     |     | A or B |     | 1   | 5.5 | 1.6 | 5.5 | ns  |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
dis
(1) The propagation delay is the calculated RC time constant of the typical on-state resistance of the switch and the specified load
capacitance, when driven by an ideal voltage source (zero output impedance).
Copyright © 2026 Texas Instruments Incorporated Submit Document Feedback 7
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
| SCDS040N – DECEMBER 1997 – REVISED JULY 2026 |     |     |     |     | www.ti.com |
| -------------------------------------------- | --- | --- | --- | --- | ---------- |
5.8 Switching Characteristics - DYY and BQB Package only
over recommended operating free-air temperature range -40 to 125°C (unless otherwise noted) (See Figure 6-1)
|           |              |             | V CC  = 2.5 ± 0.2V | V CC  = 3.3V ± 0.3V |      |
| --------- | ------------ | ----------- | ------------------ | ------------------- | ---- |
| PARAMETER | FROM (INPUT) | TO (OUTPUT) |                    |                     | UNIT |
|           |              |             | MIN                | MAX MIN             | MAX  |
|           | A or B(1)    | B or A      |                    | 3                   | 1.6  |
| t         |              |             |                    |                     | ns   |
pd
|      | S   | A   | 0.6 | 3 0.5   | 1.6    |
| ---- | --- | --- | --- | ------- | ------ |
| t en | S   | B   | 3.8 | 6.6 3.2 | 5.6 ns |
| t    | S   | B   | 3.8 | 6.5 3.3 | 5.5 ns |
dis
| t   | OE  | A or B | 5   | 6.5 4.5 | 5.6 ns |
| --- | --- | ------ | --- | ------- | ------ |
en
| t dis | OE  | A or B | 4.6 | 6.4 4.3 | 5.2 ns |
| ----- | --- | ------ | --- | ------- | ------ |
5.9 Typical Characteristics
|     | RONvs Input Voltage    |     | RONvs Input Voltage    |     |     |
| --- | ---------------------- | --- | ---------------------- | --- | --- |
|     | VDD= 2.5 V, IDS= 15 mA |     | VDD= 3.3 V, IDS= 64 mA |     |     |
24 15
14 TA = -40 C
22 TA=-40C
| 20 TA=25C |     | 13  | TA = 25 C |     |     |
| ---------- | --- | --- | ---------- | --- | --- |
TA=85C 12 TA = 85 C
| 18 TA=125C |     | 11  | TA = 125 C |     |     |
| ----------- | --- | --- | ----------- | --- | --- |
10
)(NOR 16 )(NOR 9
14 8
7
12
10 6
5
8 4
6 3
2
4 1
2 0
0 0.25 0.5 0.75 1 1.25 1.5 1.75 2 2.25 2.5 0 0.25 0.5 0.75 1 1.25 1.5 1.75 2 2.25 2.5 2.75 3 3.25 3.5
|     | Input Voltage (V) |     |     | Input Voltage (V) |     |
| --- | ----------------- | --- | --- | ----------------- | --- |
Figure 5-1. V  = 2.5V, I  = 15mA Figure 5-2. V  = 3.3V, I  = 64mA
|     | DD DS |     |     | DD DS |     |
| --- | ----- | --- | --- | ----- | --- |
8 Submit Document Feedback Copyright © 2026 Texas Instruments Incorporated
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
| www.ti.com |     |     |     |     |     |     | SCDS040N – DECEMBER 1997 – REVISED JULY 2026 |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
6 Parameter Measurement Information
|     |     |     |     | 2×VCC |     |     |           | TEST |      | S1  |     |
| --- | --- | --- | --- | ----- | --- | --- | --------- | ---- | ---- | --- | --- |
|     |     |     | S1  |       |     |     | tPLH/tPHL |      | Open |     |     |
|     |     | RL  |     | Open  |     |     |           |      |      |     |     |
FromOutput
|     |     |     |     | GND |     |     | tPLZ/tPZL |     | 2×VCC |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----- | --- | --- |
UnderTest
|     |     |     |     |     |     |     | tPHZ/tPZH |     |     | GND |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
CL
| (see NoteA) |     | RL  |     |     |     |            |     |       |     |      |        |
| ----------- | --- | --- | --- | --- | --- | ---------- | --- | ----- | --- | ---- | ------ |
|             |     |     |     |     |     | VCC        |     | CL    |     | RL   | V∆     |
|             |     |     |     |     |     | 2.5 V±0.2V |     | 30 pF |     | 500Ω | 0.15 V |
|             |     |     |     |     |     | 3.3 V±0.3V |     | 50 pF |     | 500Ω | 0.3 V  |
LOAD CIRCUIT
VCC
|     |     |     |     |     | Timing Input |     |     |     | VCC/2 |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ----- | --- | --- |
0 V
tw
|     |     |     |     |     |     |     |     | tsu | th  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
VCC
VCC
| Input |     | VCC/2 |     | VCC/2 |     |     |     | VCC/2 |     |     | VCC/2 |
| ----- | --- | ----- | --- | ----- | --- | --- | --- | ----- | --- | --- | ----- |
Data Input
|     |                  |               |     | 0 V |     |     |                     |     |     |     | 0 V |
| --- | ---------------- | ------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
|     | VOLTAGEWAVEFORMS |               |     |     |     |     | VOLTAGEWAVEFORMS    |     |     |     |     |
|     |                  | PULSEDURATION |     |     |     |     | SETUPAND HOLD TIMES |     |     |     |     |
|     |                  |               |     | VCC |     |     |                     |     |     |     | VCC |
Output
|       |     | VCC/2 | VCC/2 |     |     |         |     | VCC/2 |     | VCC/2 |     |
| ----- | --- | ----- | ----- | --- | --- | ------- | --- | ----- | --- | ----- | --- |
| Input |     |       |       |     |     | Control |     |       |     |       |     |
0 V
0 V
|     | tPLH |     |     | tPHL |     | tPZL |     |     |     |     | tPLZ |
| --- | ---- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | ---- |
Output
VOH
|        |     |       |     |       | Waveform 1  |     |     |       |     |         | VCC |
| ------ | --- | ----- | --- | ----- | ----------- | --- | --- | ----- | --- | ------- | --- |
|        |     | VCC/2 |     | VCC/2 |             |     |     | VCC/2 |     |         |     |
| Output |     |       |     |       | S1 at 2×VCC |     |     |       |     | VOL+ V∆ |     |
VOL
|     |      |     |     |      | (see Note B) |      |     |     |     |     | VOL  |
| --- | ---- | --- | --- | ---- | ------------ | ---- | --- | --- | --- | --- | ---- |
|     | tPHL |     |     | tPLH |              | tPZH |     |     |     |     | tPHZ |
Output
|        |     |       |     | VOH   |            |     |     |       |     |        | VOH  |
| ------ | --- | ----- | --- | ----- | ---------- | --- | --- | ----- | --- | ------ | ---- |
|        |     |       |     |       | Waveform 2 |     |     |       |     | VOH−V∆ |      |
|        |     | VCC/2 |     | VCC/2 |            |     |     | VCC/2 |     |        |      |
| Output |     |       |     |       | S1 at GND  |     |     |       |     |        |      |
|        |     |       |     | VOL   |            |     |     |       |     |        | ≈0 V |
(see Note B)
|                                   | VOLTAGEWAVEFORMS                         |     |     |     |     |                            | VOLTAGEWAVEFORMS        |     |     |     |     |
| --------------------------------- | ---------------------------------------- | --- | --- | --- | --- | -------------------------- | ----------------------- | --- | --- | --- | --- |
|                                   | PROPAGATIONDELAYTIMES                    |     |     |     |     |                            | ENABLEAND DISABLE TIMES |     |     |     |     |
| INVERTINGAND NONINVERTING OUTPUTS |                                          |     |     |     |     | LOW-AND HIGH-LEVELENABLING |                         |     |     |     |     |
| NOTES:                            | A. CLincludes probe and jig capacitance. |     |     |     |     |                            |                         |     |     |     |     |
B. Waveform 1 is for an output with internal conditions such that the output is low except when disabled by the output control.
Waveform2isforanoutputwithinternalconditionssuchthattheoutputishighexceptwhendisabledbytheoutputcontrol.
C. All input pulses are supplied by generators having the following characteristics: PRR≤10 MHz, ZO= 50Ω, tr ≤2ns,tf ≤2 ns.
|     | D. Theoutputsaremeasuredoneatatimewithonetransitionpermeasurement. |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | E. tPLZand tPHZare the same as tdis.                               |     |     |     |     |     |     |     |     |     |     |
|     | F. tPZLand tPZHare the same as ten.                                |     |     |     |     |     |     |     |     |     |     |
|     | G. tPLHand tPHLare the same as tpd.                                |     |     |     |     |     |     |     |     |     |     |
|     | H. Allparametersandwaveformsarenotapplicabletoalldevices.          |     |     |     |     |     |     |     |     |     |     |
Figure 6-1. Load Circuit and Voltage Waveforms
Copyright © 2026 Texas Instruments Incorporated Submit Document Feedback 9
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
SCDS040N – DECEMBER 1997 – REVISED JULY 2026 www.ti.com
7 Detailed Description
7.1 Overview
The SN74CBTLV3257 device is a 4-bit 1-of-2 high-speed FET multiplexer and demultiplexer. The low ON-state
resistance of the switch allows connections to be made with minimal propagation delay.
The select (S) input controls the data flow. The FET multiplexers and demultiplexers are disabled when the
output-enable ( OE) input is high.
This device is fully specified for partial-power-down applications using I off . The I off  feature ensures that damaging
current will not backflow through the device when it is powered down. The device has isolation during power off.
To ensure the high-impedance state during power up or power down, OE must be tied to V CC  through a pullup
resistor; the minimum value of the resistor is determined by the current-sinking capability of the driver.
7.2 Functional Block Diagram
| 4   |     | 2   |
| --- | --- | --- |
| 1A  | SW  | 1B1 |
3
|     | SW  | 1B2 |
| --- | --- | --- |
| 7   |     | 5   |
| 2A  | SW  | 2B1 |
6
|     | SW  | 2B2 |
| --- | --- | --- |
| 9   |     | 11  |
| 3A  | SW  | 3B1 |
10
|     | SW  | 3B2 |
| --- | --- | --- |
| 12  |     | 14  |
| 4A  | SW  | 4B1 |
13
|     | SW  | 4B2 |
| --- | --- | --- |
1
S
15
OE
7.3 Feature Description
The SN74CBTLV3257 features 5Ω switch connection between ports, allowing for low signal loss across the
switch. Rail-to-rail switching on data I/O allows for full voltage swing outputs. I  supports partial-power-down
off
mode  operation,  protecting  the  chip  from  voltages  at  output  ports  when  it  is  not  powered  on.  Latch-up
performance exceeds 100mA per JESD 78, Class II.
7.4 Device Functional Modes
Table 7-1 shows the functional modes of SN74CBTLV3257.
Table 7-1. Function Table
INPUTS
FUNCTION
OE  S
| L L | A port = B1 port |     |
| --- | ---------------- | --- |
| L H | A port = B2 port |     |
| H X | Disconnect       |     |
10 Submit Document Feedback Copyright © 2026 Texas Instruments Incorporated
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
www.ti.com SCDS040N – DECEMBER 1997 – REVISED JULY 2026
8 Application and Implementation
Note
Information in the following applications sections is not part of the TI component specification, and
TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining
suitability of components for their purposes. Customers should validate and test their design
implementation to confirm system functionality.
8.1 Application Information
The SN74CBTLV3257 can be used to multiplex and demultiplex up to 4 channels simultaneously in a 2:1
configuration. The application shown here is a 4-bit bus being multiplexed between two devices. the OE and S
pins are used to control the chip from the bus controller. This is a very generic example, and could apply to many
situations. If an application requires less than 4 bits, be sure to tie the A side to either high or low on unused
channels.
8.2 Typical Application
V
CC
SN74CBTLV3257 V
CC
16
S
1 0.1 PF
1B1
2
1A R
ON
4
1B2
3
2B1 4
5 Device 1
2A R
ON
7
2B2
6
Bus 4
Controller 3B1
11
3A R
ON
9
3B2
10 4
Device 2
4B1
14
4A R
ON
12
4B2
13
GND OE
8 15
Figure 8-1. Typical Application of the SN74CBTLV3257
Copyright © 2026 Texas Instruments Incorporated Submit Document Feedback 11
Product Folder Links: SN74CBTLV3257

8.2.1 Design Requirements
1. Recommended Input Conditions:
• For specified high and low levels, see V and V in Section 5.4.
IH IL
• Inputs and outputs are overvoltage tolerant slowing them to go as high as 4.6V at any valid V .
CC
2. Recommended Output Conditions:
• Load currents must not exceed ±128mA per channel.
3. Frequency Selection Criterion:
• Maximum frequency tested is 200MHz.
• Added trace resistance/capacitance can reduce maximum frequency capability; use layout practices as
directed in Section 8.4.
8.2.2 Detailed Design Procedure
The 4-bit bus is connected directly to the 1A, 2A, 3A, and 4A ports (known as the xA port) on the
SN74CBTLV3257, which essentially splits it into two busses, coming out of the xB1 and xB2 ports. When S
is high, xB2 is the active bus, and when S is low, xB1 is the active bus. This means that Device 2 is connected
to the bus controller when S is high, and Device 1 is connected to the bus controller when S is low. This setup
is especially useful when two devices are hard coded with the same address and only one bus is available. The
OE connection can be used to disconnect all devices from the bus controller if necessary.
The 0.1µF capacitor on V is a decoupling capacitor and must be placed as close as possible to the device.
CC
8.2.3 Application Curve
3
2
1
0
0 1 2 3 4 5
)V(
egatloV
SN74CBTLV3257
SCDS040N – DECEMBER 1997 – REVISED JULY 2026 www.ti.com
Input
Output
Time (ns)
C001
Figure 8-2. Propagation Delay (t ) Simulation Result at V = 2.5V
pd CC
8.3 Power Supply Recommendations
The power supply can be any voltage between the minimum and maximum supply voltage rating listed in the
Section 5.4 table.
Each V terminal should have a good bypass capacitor to prevent power disturbance. For devices with a
CC
single supply, a 0.1μF bypass capacitor is recommended. If multiple pins are labeled V , then a 0.01μF or
CC
0.022μF capacitor is recommended for each V because the V pins are tied together internally. For devices
CC CC
with dual-supply pins operating at different voltages, for example V and V , a 0.1µF bypass capacitor is
CC DD
recommended for each supply pin. To reject different frequencies of noise, use multiple bypass capacitors in
parallel. Capacitors with values of 0.1μF and 1μF are commonly used in parallel. The bypass capacitor must be
installed as close to the power terminal as possible for best results.
12 Submit Document Feedback Copyright © 2026 Texas Instruments Incorporated
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
www.ti.com SCDS040N – DECEMBER 1997 – REVISED JULY 2026
8.4 Layout
8.4.1 Layout Guidelines
Reflections and matching are closely related to the loop antenna theory but are different enough to be discussed
separately from the theory. When a PCB trace turns a corner at a 90° angle, a reflection can occur. A reflection
occurs primarily because of the change of width of the trace. At the apex of the turn, the trace width increases
to 1.414 times the width. This increase upsets the transmission-line characteristics, especially the distributed
capacitance and self–inductance of the trace which results in the reflection. Not all PCB traces can be straight
and therefore some traces must turn corners. Figure 8-3 shows progressively better techniques of rounding
corners. Only the last example (BEST) maintains constant trace width and minimizes reflections.
8.4.2 Layout Example
WORST BETTER BEST
W
2
1W min.
W
Figure 8-3. Trace Example
Copyright © 2026 Texas Instruments Incorporated Submit Document Feedback 13
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
SCDS040N – DECEMBER 1997 – REVISED JULY 2026 www.ti.com
9 Device and Documentation Support
9.1 Documentation Support
9.1.1 Related Documentation
For related documentation see the following:
• Texas Instruments, Implications of Slow or Floating CMOS Inputs application report
• Texas Instruments, Selecting the Right Texas Instruments Signal Switch application note
9.2 Receiving Notification of Documentation Updates
To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on
Notifications to register and receive a weekly digest of any product information that has changed. For change
details, review the revision history included in any revised document.
9.3 Support Resources
TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help — straight
from the experts. Search existing answers or ask your own question to get the quick design help you need.
Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
not necessarily reflect TI's views; see TI's Terms of Use.
9.4 Trademarks
TI E2E™ is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.
9.5 Electrostatic Discharge Caution
This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.
9.6 Glossary
TI Glossary This glossary lists and explains terms, acronyms, and definitions.
14 Submit Document Feedback Copyright © 2026 Texas Instruments Incorporated
Product Folder Links: SN74CBTLV3257

SN74CBTLV3257
www.ti.com SCDS040N – DECEMBER 1997 – REVISED JULY 2026
10 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision M (July 2018) to Revision N (July 2026) Page
• Added additional applications.............................................................................................................................1
• Updated Thermal ratings ...................................................................................................................................5
• Added Electrical Specification section for new package ...................................................................................7
• Added Switching Specification section for new package....................................................................................8
• Added Typical Curves ........................................................................................................................................8
Changes from Revision L (October 2016) to Revision M (July 2018) Page
• Changed the pin images appearance ................................................................................................................3
Changes from Revision K (April 2015) to Revision L (October 2016) Page
• Added TSSOP (16) to Device Information table.................................................................................................1
• Added Junction temperature, T in Absolute Maximum Ratings .......................................................................5
J
• Changed wording in Detailed Design Procedure to clarify device operation....................................................12
• Added Receiving Notification of Documentation Updates section and Community Resources section...........15
Changes from Revision J (December 2012) to Revision K (April 2015) Page
• Removed Ordering Information table, see Mechanical, Packaging, and Orderable Information .......................1
• Added Pin Configuration and Functions section, ESD Ratings table, Feature Description section, Device
Functional Modes, Application and Implementation section, Power Supply Recommendations section, Layout
section, Device and Documentation Support section, and Mechanical, Packaging, and Orderable Information
section ...............................................................................................................................................................1
• Added Applications.............................................................................................................................................1
• Added Device Information table.........................................................................................................................1
Changes from Revision I (October 2003) to Revision J (December 2012) Page
• Added QFN ordering info and package pinout ..................................................................................................1
• Added New Packages with 125°C capability .....................................................................................................6
11 Mechanical, Packaging, and Orderable Information
The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
Copyright © 2026 Texas Instruments Incorporated Submit Document Feedback 15
Product Folder Links: SN74CBTLV3257

PACKAGE OPTION ADDENDUM
www.ti.com 18-Sep-2026
PACKAGING INFORMATION
Orderable part number Status Material type Package | Pins Package qty | Carrier RoHS Lead finish/ MSL rating/ Op temp (°C) Part marking
(1) (2) (3) Ball material Peak reflow (6)
(4) (5)
74CBTLV3257DBQRG4 Active Production SSOP (DBQ) | 16 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 CL257
74CBTLV3257DBQRG4.A Active Production SSOP (DBQ) | 16 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 CL257
74CBTLV3257DBQRG4.B Active Production SSOP (DBQ) | 16 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 CL257
74CBTLV3257DGVRG4 Active Production TVSOP (DGV) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
74CBTLV3257DGVRG4.B Active Production TVSOP (DGV) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
74CBTLV3257PWRE4 Active Production TSSOP (PW) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
74CBTLV3257PWRG4 Active Production TSSOP (PW) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
74CBTLV3257PWRG4.B Active Production TSSOP (PW) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
74CBTLV3257RSVRG4 Active Production UQFN (RSV) | 16 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 ZTR
74CBTLV3257RSVRG4.A Active Production UQFN (RSV) | 16 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 ZTR
74CBTLV3257RSVRG4.B Active Production UQFN (RSV) | 16 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 ZTR
SN74CBTLV3257BQBR Active Production WQFN (BQB) | 16 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
SN74CBTLV3257D Obsolete Production SOIC (D) | 16 - - Call TI Call TI -40 to 85 CBTLV3257
SN74CBTLV3257DBQR Active Production SSOP (DBQ) | 16 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 CL257
SN74CBTLV3257DBQR.A Active Production SSOP (DBQ) | 16 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 CL257
SN74CBTLV3257DBQR.B Active Production SSOP (DBQ) | 16 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 CL257
SN74CBTLV3257DGVR Active Production TVSOP (DGV) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
SN74CBTLV3257DGVR.B Active Production TVSOP (DGV) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
SN74CBTLV3257DR Active Production SOIC (D) | 16 2500 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CBTLV3257
SN74CBTLV3257DR.A Active Production SOIC (D) | 16 2500 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CBTLV3257
SN74CBTLV3257DR.B Active Production SOIC (D) | 16 2500 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CBTLV3257
SN74CBTLV3257DYYR Active Production SOT-23-THIN 3000 | LARGE T&R Yes Call TI Level-1-260C-UNLIM -40 to 85 CL257
(DYY) | 16
SN74CBTLV3257PWR Active Production TSSOP (PW) | 16 2000 | LARGE T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 85 CL257
SN74CBTLV3257PWR.A Active Production TSSOP (PW) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
SN74CBTLV3257PWR.B Active Production TSSOP (PW) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
SN74CBTLV3257PWRG4 Active Production TSSOP (PW) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
SN74CBTLV3257PWRG4.A Active Production TSSOP (PW) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
SN74CBTLV3257PWRG4.B Active Production TSSOP (PW) | 16 2000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 CL257
Addendum-Page 1

PACKAGE OPTION ADDENDUM
www.ti.com 18-Sep-2026
Orderable part number Status Material type Package | Pins Package qty | Carrier RoHS Lead finish/ MSL rating/ Op temp (°C) Part marking
(1) (2) (3) Ball material Peak reflow (6)
(4) (5)
SN74CBTLV3257RGYR Active Production VQFN (RGY) | 16 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 CL257
SN74CBTLV3257RGYR.A Active Production VQFN (RGY) | 16 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 CL257
SN74CBTLV3257RGYR.B Active Production VQFN (RGY) | 16 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 CL257
SN74CBTLV3257RSVR Active Production UQFN (RSV) | 16 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 ZTR
SN74CBTLV3257RSVR.A Active Production UQFN (RSV) | 16 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 ZTR
SN74CBTLV3257RSVR.B Active Production UQFN (RSV) | 16 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 85 ZTR
(1) Status: For more details on status, see our product life cycle.
(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.
(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.
(4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum
column width.
(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown.
Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.
(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.
Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two
combined represent the entire part marking for that device.
Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.
In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.
OTHER QUALIFIED VERSIONS OF SN74CBTLV3257 :
Addendum-Page 2

PACKAGE OPTION ADDENDUM
www.ti.com 18-Sep-2026
•Automotive : SN74CBTLV3257-Q1
•Enhanced Product : SN74CBTLV3257-EP
NOTE: Qualified Version Definitions:
•Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects
•Enhanced Product - Supports Defense, Aerospace and Medical Applications
Addendum-Page 3

PACKAGE MATERIALS INFORMATION
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
www.ti.com 9-Nov-2026
TAPE AND REEL INFORMATION
| REEL DIMENSIONS |     |     | TAPE DIMENSIONS |     |     |     |
| --------------- | --- | --- | --------------- | --- | --- | --- |
K0  P1
W
B0
Reel
Diameter
|     |     |     | Cavity                                                    | A0  |     |     |
| --- | --- | --- | --------------------------------------------------------- | --- | --- | --- |
|     |     | A0  | Dimension designed to accommodate the component width     |     |     |     |
|     |     | B0  | Dimension designed to accommodate the component length    |     |     |     |
|     |     | K0  | Dimension designed to accommodate the component thickness |     |     |     |
|     |     | W   | Overall width of the carrier tape                         |     |     |     |
|     |     | P1  | Pitch between successive cavity centers                   |     |     |     |
Reel Width (W1)
QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE
Sprocket Holes
|     |     | Q1 Q2 | Q1 Q2 |                        |     |     |
| --- | --- | ----- | ----- | ---------------------- | --- | --- |
|     |     | Q3 Q4 | Q3 Q4 | User Direction of Feed |     |     |
Pocket Quadrants

*All dimensions are nominal
| Device | Package Package | Pins | SPQ Reel Reel | A0 B0 | K0 P1 | W Pin1 |
| ------ | --------------- | ---- | ------------- | ----- | ----- | ------ |
Type Drawing Diameter Width (mm) (mm) (mm) (mm) (mm) Quadrant
|     |     |     | (mm) W1 (mm) |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- |
74CBTLV3257DBQRG4 SSOP DBQ 16 2500 330.0 12.5 6.4 5.2 2.1 8.0 12.0 Q1
74CBTLV3257DGVRG4 TVSOP DGV 16 2000 330.0 12.4 6.8 4.0 1.6 8.0 12.0 Q1
74CBTLV3257PWRG4 TSSOP PW 16 2000 330.0 12.4 6.9 5.6 1.6 8.0 12.0 Q1
74CBTLV3257RSVRG4 UQFN RSV 16 3000 180.0 13.2 2.1 2.9 0.75 4.0 12.0 Q1
SN74CBTLV3257BQBR WQFN BQB 16 3000 180.0 12.4 2.8 3.8 1.2 4.0 12.0 Q1
SN74CBTLV3257DBQR SSOP DBQ 16 2500 330.0 12.4 6.4 5.2 2.1 8.0 12.0 Q1
SN74CBTLV3257DBQR SSOP DBQ 16 2500 330.0 12.5 6.4 5.2 2.1 8.0 12.0 Q1
SN74CBTLV3257DGVR TVSOP DGV 16 2000 330.0 12.4 6.8 4.0 1.6 8.0 12.0 Q1
SN74CBTLV3257DR SOIC D 16 2500 330.0 16.4 6.5 10.3 2.1 8.0 16.0 Q1
SN74CBTLV3257DYYR SOT-23- DYY 16 3000 330.0 12.4 4.5 3.56 1.35 8.0 12.0 Q3
THIN
SN74CBTLV3257PWR TSSOP PW 16 2000 330.0 12.4 6.9 5.6 1.6 8.0 12.0 Q1
SN74CBTLV3257PWR TSSOP PW 16 2000 330.0 12.4 6.9 5.6 1.6 8.0 12.0 Q1
SN74CBTLV3257PWR TSSOP PW 16 2000 330.0 12.4 6.9 5.6 1.6 8.0 12.0 Q1
SN74CBTLV3257PWR TSSOP PW 16 2000 330.0 12.4 6.9 5.3 1.6 8.0 12.0 Q1
SN74CBTLV3257PWRG4 TSSOP PW 16 2000 330.0 12.4 6.9 5.6 1.6 8.0 12.0 Q1
Pack Materials-Page 1

PACKAGE MATERIALS INFORMATION
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
www.ti.com 9-Nov-2026
| Device | Package Package | Pins SPQ | Reel Reel | A0 B0 | K0 P1 | W Pin1 |
| ------ | --------------- | -------- | --------- | ----- | ----- | ------ |
Type Drawing Diameter Width (mm) (mm) (mm) (mm) (mm) Quadrant
(mm) W1 (mm)
SN74CBTLV3257RGYR VQFN RGY 16 3000 330.0 12.4 3.8 4.3 1.5 8.0 12.0 Q1
SN74CBTLV3257RGYR VQFN RGY 16 3000 330.0 12.4 3.8 4.3 1.5 8.0 12.0 Q1
SN74CBTLV3257RSVR UQFN RSV 16 3000 180.0 13.2 2.1 2.9 0.75 4.0 12.0 Q1
Pack Materials-Page 2

PACKAGE MATERIALS INFORMATION
|            |     |     |     |     |     |            |
| ---------- | --- | --- | --- | --- | --- | ---------- |
| www.ti.com |     |     |     |     |     | 9-Nov-2026 |
TAPE AND REEL BOX DIMENSIONS
Width (mm)
H
W L

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
| 74CBTLV3257DBQRG4  | SSOP        | DBQ | 16 2500 | 353.0 | 353.0 | 32.0 |
| ------------------ | ----------- | --- | ------- | ----- | ----- | ---- |
| 74CBTLV3257DGVRG4  | TVSOP       | DGV | 16 2000 | 353.0 | 353.0 | 32.0 |
| 74CBTLV3257PWRG4   | TSSOP       | PW  | 16 2000 | 353.0 | 353.0 | 32.0 |
| 74CBTLV3257RSVRG4  | UQFN        | RSV | 16 3000 | 180.0 | 180.0 | 30.0 |
| SN74CBTLV3257BQBR  | WQFN        | BQB | 16 3000 | 210.0 | 185.0 | 35.0 |
| SN74CBTLV3257DBQR  | SSOP        | DBQ | 16 2500 | 353.0 | 353.0 | 32.0 |
| SN74CBTLV3257DBQR  | SSOP        | DBQ | 16 2500 | 353.0 | 353.0 | 32.0 |
| SN74CBTLV3257DGVR  | TVSOP       | DGV | 16 2000 | 353.0 | 353.0 | 32.0 |
| SN74CBTLV3257DR    | SOIC        | D   | 16 2500 | 353.0 | 353.0 | 32.0 |
| SN74CBTLV3257DYYR  | SOT-23-THIN | DYY | 16 3000 | 360.0 | 360.0 | 36.0 |
| SN74CBTLV3257PWR   | TSSOP       | PW  | 16 2000 | 364.0 | 364.0 | 27.0 |
| SN74CBTLV3257PWR   | TSSOP       | PW  | 16 2000 | 353.0 | 353.0 | 32.0 |
| SN74CBTLV3257PWR   | TSSOP       | PW  | 16 2000 | 356.0 | 356.0 | 35.0 |
| SN74CBTLV3257PWR   | TSSOP       | PW  | 16 2000 | 367.0 | 367.0 | 35.0 |
| SN74CBTLV3257PWRG4 | TSSOP       | PW  | 16 2000 | 353.0 | 353.0 | 32.0 |
| SN74CBTLV3257RGYR  | VQFN        | RGY | 16 3000 | 360.0 | 360.0 | 36.0 |
| SN74CBTLV3257RGYR  | VQFN        | RGY | 16 3000 | 353.0 | 353.0 | 32.0 |
| SN74CBTLV3257RSVR  | UQFN        | RSV | 16 3000 | 180.0 | 180.0 | 30.0 |
Pack Materials-Page 3

PACKAGE OUTLINE
RGY0016A VQFN - 1 mm max height
SCALE 3.000
PLASTIC QUAD FLATPACK - NO LEAD
3.65
B A
3.35
PIN 1 INDEX AREA
4.15
3.85
1.0
0.8
C
SEATING PLANE
0.05 0.08 C
0.00
2.05 0.1
2X 1.5
SYMM
(0.2) TYP
8 9
EXPOSED
THERMAL PAD
7 10
SYMM 17
2X 2.5 2.55 0.1
10X 0.5
2
15 0.30
16X
0.18
PIN 1 ID 1 16 0.1 C A B
0.5 0.05
16X
0.3
4225140/A 07/2019
NOTES:
1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
www.ti.com

EXAMPLE BOARD LAYOUT
RGY0016A VQFN - 1 mm max height
PLASTIC QUAD FLATPACK - NO LEAD
(2.05)
2X (1.5)
SYMM
1 16 SEE SOLDER MASK
DETAIL
16X (0.6)
15
16X (0.24) 2
(2.55)
10X (0.5)
17 SYMM
(3.8)
(1.025)
10
7
(R0.05) TYP
( 0.2) TYP
VIA
8 9
(0.775)
(3.3)
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 20X
0.07 MIN
0.07 MAX
ALL AROUND
ALL AROUND
METAL UNDER
METAL EDGE
SOLDER MASK
EXPOSED METAL
SOLDER MASK EXPOSED SOLDER MASK
OPENING METAL OPENING
NON SOLDER MASK
DEFINED SOLDER MASK DEFINED
(PREFERRED)
SOLDER MASK DETAILS
4225140/A 07/2019
NOTES: (continued)
4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
on this view. It is recommended that vias under paste be filled, plugged or tented.
www.ti.com

EXAMPLE STENCIL DESIGN
RGY0016A VQFN - 1 mm max height
PLASTIC QUAD FLATPACK - NO LEAD
2X (1.5)
(0.56) TYP
1 16
16X (0.6)
16X (0.24) 2 15
10X (0.5)
(0.665) TYP
17
SYMM
(3.8)
(R0.05) TYP
4X (1.13)
7
10
8 9
4X (0.92)
SYMM
(3.3)
SOLDER PASTE EXAMPLE
BASED ON 0.125 MM THICK STENCIL
SCALE: 20X
EXPOSED PAD 17
80% PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE
4225140/A 07/2019
NOTES: (continued)
6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
www.ti.com

GENERIC PACKAGE VIEW
RSV 16 UQFN - 0.55 mm max height
1.8 x 2.6, 0.4 mm pitch ULTRA THIN QUAD FLATPACK - NO LEAD
This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.
4231225/A
www.ti.com

MECHANICAL DATA
MPDS006C – FEBRUARY 1996 – REVISED AUGUST 2000
DGV (R-PDSO-G**) PLASTIC SMALL-OUTLINE
24 PINS SHOWN
0,23
0,40 0,07 M
0,13
24 13
0,16 NOM
4,50 6,60
4,30 6,20
Gage Plane
0,25
0°–(cid:1)8°
0,75
1 12
0,50
A
Seating Plane
0,15
1,20 MAX 0,08
0,05
PINS **
14 16 20 24 38 48 56
DIM
A MAX 3,70 3,70 5,10 5,10 7,90 9,80 11,40
A MIN 3,50 3,50 4,90 4,90 7,70 9,60 11,20
4073251/E 08/00
NOTES: A. All linear dimensions are in millimeters.
B. This drawing is subject to change without notice.
C. Body dimensions do not include mold flash or protrusion, not to exceed 0,15 per side.
D. Falls within JEDEC: 24/48 Pins – MO-153
14/16/20/56 Pins – MO-194
•
POST OFFICE BOX 655303 DALLAS, TEXAS 75265

GENERIC PACKAGE VIEW
BQB 16 WQFN - 0.8 mm max height
2.5 x 3.5, 0.5 mm pitch PLASTIC QUAD FLATPACK - NO LEAD
This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.
4226161/A
www.ti.com

PACKAGE OUTLINE
BQB0016A WQFN - 0.8 mm max height
PLASTIC QUAD FLAT PACK-NO LEAD
2.6 A
B
2.4
3.6
3.4
PIN 1 INDEX AREA
(0.23)
(0.16) (0.15) TYP
NOTE 4
0.8 C
0.7
SEATING PLANE
1.1 0.08 C
0.05 0.9
0.00
2X 0.5 (0.2) TYP
8 9
10X 0.5
7
10
SYMM
2X 2.1
2.5 1.9
15
2
0.30
16X
PIN 1 ID 1 16 0.18
(OPTIONAL) SYMM 16X 0 0 . . 5 3 0.1 C A B
0.05 C
4224640/B 01/2026
NOTES:
1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for optimal thermal and mechanical performance.
4. Features may differ or may not be present
www.ti.com

EXAMPLE BOARD LAYOUT
BQB0016A WQFN - 0.8 mm max height
PLASTIC QUAD FLAT PACK-NO LEAD
(2.3)
(1)
2X (0.5)
1 16
10X (0.5)
2 15
SYMM
2X
(2) (3.3)
(2.5)
2X
(0.75)
10
7
16X (0.24)
(Ø0.2) VIA
TYP 16X (0.6)
8 9
SYMM
(R0.05) TYP
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 20X
0.07 MAX 0.07 MIN METAL UNDER
ALL AROUND ALL AROUND SOLDER MASK
METAL
EXPOSED METAL
SOLDER MASK SOLDER MASK
EXPOSED METAL
OPENING OPENING
NON-SOLDER MASK
SOLDER MASK
DEFINED
DEFINED
(PREFERRED)
4224640/B 01/2026
1. NOTES: (continued)
5. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments
literature number SLUA271 (www.ti.com/lit/slua271).
6. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations
shown on this view. It is recommended that vias under paste be filled, plugged or tented.
www.ti.com

EXAMPLE STENCIL DESIGN
BQB0016A WQFN - 0.8 mm max height
PLASTIC QUAD FLAT PACK-NO LEAD
(2.3)
(0.95)
2X (0.5)
1 16
10X (0.5)
2 15
SYMM
2X
(1.79) (3.3)
(2.5)
10
7
16X (0.24)
EXPOSED METAL
16X (0.6)
8 9
SYMM
(R0.05) TYP
SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL
EXPOSED PAD
85% PRINTED COVERAGE BY AREA
SCALE: 20X
4224640/B 01/2026
NOTES: (continued)
7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
www.ti.com

PACKAGE OUTLINE
DYY0016A SOT-23-THIN - 1.1 mm max height
PLASTIC SMALL OUTLINE
3.36 C
3.16 SEATING PLANE
A PIN 1 INDEX
AREA 0.1 C
14X 0.5
16
1
4.3 2X
4.1
NOTE 3 3.5
4X 0° - 15°
8
9
0.3 1.1 MAX
2.1 16X
B 0.11
1.9
0.1 C A B
4X 4° - 15°
0.2
TYP
0.08
SEE DETAIL A
0.25
GAUGE PLANE
0°- 8°
0.63 0.1
0.33 0.0
DETAIL A
TYP
4224642/D 07/2024
NOTES:
1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed
0.15 per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.50 per side.
5. Reference JEDEC Registration MO-345, Variation AA
www.ti.com

EXAMPLE BOARD LAYOUT
DYY0016A SOT-23-THIN - 1.1 mm max height
PLASTIC SMALL OUTLINE
16X (1.05)
SYMM
1 16
16X (0.3)
SYMM
14X (0.5)
9
8
(R0.05) TYP
(3)
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 20X
SOLDER MASK METAL UNDER
OPENING SOLDER MASK SOLDER MASK
METAL OPENING
NON- SOLDER MASK SOLDER MASK
DEFINED DEFINED
(PREFERRED)
SOLDER MASK DETAILS
4224642/D 07/2024
NOTES: (continued)
6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
www.ti.com

EXAMPLE STENCIL DESIGN
DYY0016A SOT-23-THIN - 1.1 mm max height
PLASTIC SMALL OUTLINE
16X (1.05)
SYMM
1 16
16X (0.3)
SYMM
14X (0.5)
9
8
(R0.05) TYP
(3)
SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL
SCALE: 20X
4224642/D 07/2024
NOTES: (continued)
8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.
www.ti.com

PACKAGE OUTLINE
PW0016A TSSOP - 1.2 mm max height
SCALE 2.500
SMALL OUTLINE PACKAGE
SEATING
PLANE
C
6.6
TYP
6.2
A
0.1 C
PIN 1 INDEX AREA
14X 0.65
16
1
2X
5.1 4.55
4.9
NOTE 3
4X (0 -12 )
8
9
0.30
B 4.5 16X 0.17 1.2 MAX
4.3
0.1 C A B
NOTE 4
(0.15) TYP
SEE DETAIL A
0.25
GAGE PLANE
0.15
0.05
0.75
0.50
0 -8
DETA 20AIL A
TYPICAL
4220204/B 12/2023
NOTES:
1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-153.
www.ti.com

EXAMPLE BOARD LAYOUT
PW0016A TSSOP - 1.2 mm max height
SMALL OUTLINE PACKAGE
16X (1.5) SYMM
(R0.05) TYP
1
16X (0.45) 16
SYMM
14X (0.65)
8 9
(5.8)
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 10X
SOLDER MASK METAL UNDER SOLDER MASK
OPENING METAL SOLDER MASK OPENING
EXPOSED METAL EXPOSED METAL
0.05 MAX 0.05 MIN
ALL AROUND ALL AROUND
NON-SOLDER MASK SOLDER MASK
DEFINED DEFINED
(PREFERRED) SOLDE15.000R MASK DETAILS
4220204/B 12/2023
NOTES: (continued)
6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
www.ti.com

EXAMPLE STENCIL DESIGN
PW0016A TSSOP - 1.2 mm max height
SMALL OUTLINE PACKAGE
16X (1.5) SYMM
(R0.05) TYP
1
16X (0.45) 16
SYMM
14X (0.65)
8 9
(5.8)
SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL
SCALE: 10X
4220204/B 12/2023
NOTES: (continued)
8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.
www.ti.com

PACKAGE OUTLINE
DBQ0016A SSOP - 1.75 mm max height
SCALE 2.800
SHRINK SMALL-OUTLINE PACKAGE
C
SEATING PLANE
.228-.244 TYP
[5.80-6.19] .004 [0.1] C
A
PIN 1 ID AREA
14X .0250
[0.635]
16
1
2X
.189-.197
.175 [4.81-5.00]
[4.45]
NOTE 3
8
9
16X .008-.012
B .150-.157 [0.21-0.30] .069 MAX
[3.81-3.98] [1.75]
NOTE 4 .007 [0.17] C A B
.005-.010 TYP
[0.13-0.25]
SEE DETAIL A
.010 [0.25]
GAGE PLANE
.004-.010
0 - 8 [0.11-0.25]
.016-.035
[0.41-0.88] DETAIL A
(.041 ) TYPICAL
[1.04]
4214846/A 03/2014
NOTES:
1. Linear dimensions are in inches [millimeters]. Dimensions in parenthesis are for reference only. Controlling dimensions are in inches.
Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed .006 inch, per side.
4. This dimension does not include interlead flash.
5. Reference JEDEC registration MO-137, variation AB.
www.ti.com

EXAMPLE BOARD LAYOUT
DBQ0016A SSOP - 1.75 mm max height
SHRINK SMALL-OUTLINE PACKAGE
16X (.063)
[1.6]
SYMM SEE
DETAILS
1
16
16X (.016 )
[0.41]
14X (.0250 )
[0.635]
8 9
(.213)
[5.4]
LAND PATTERN EXAMPLE
SCALE:8X
SOLDER MASK SOLDER MASK
METAL OPENING OPENING METAL
.002 MAX .002 MIN
[0.05] [0.05]
ALL AROUND ALL AROUND
NON SOLDER MASK SOLDER MASK
DEFINED DEFINED
SOLDER MASK DETAILS
4214846/A 03/2014
NOTES: (continued)
6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
www.ti.com

EXAMPLE STENCIL DESIGN
DBQ0016A SSOP - 1.75 mm max height
SHRINK SMALL-OUTLINE PACKAGE
16X (.063)
[1.6]
SYMM
1
16
16X (.016 )
[0.41]
SYMM
14X (.0250 )
[0.635]
8 9
(.213)
[5.4]
SOLDER PASTE EXAMPLE
BASED ON .005 INCH [0.127 MM] THICK STENCIL
SCALE:8X
4214846/A 03/2014
NOTES: (continued)
8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.
www.ti.com

IMPORTANT NOTICE AND DISCLAIMER
TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE
DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS”
AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD
PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate
TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable
standards, and any other safety, security, regulatory or other requirements.
These resources are subject to change without notice. TI grants you permission to use these resources only for development of an
application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license
is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully
indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.
TI’s products are provided subject to TI’s Terms of Sale, TI’s General Quality Guidelines, or other applicable terms available either on
ti.com or provided in conjunction with such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable
warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products
are standard, catalog, general purpose devices.
TI objects to and rejects any additional or different terms you may propose.
IMPORTANT NOTICE
Copyright © 2026, Texas Instruments Incorporated
Last updated 10/2025
