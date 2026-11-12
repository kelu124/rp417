|     |         | 1       |                   |           |     | 2   |     |     | 3   |     |             | 4   |     |     | 5    |     | 6               |     |     | 7   |     |           | 8   |     |
| --- | ------- | ------- | ----------------- | --------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | ---- | --- | --------------- | --- | --- | --- | --- | --------- | --- | --- |
|     |         |         |                   |           |     |     |     |     |     |     | POWER&USBPD |     |     |     |      |     |                 |     |     |     |     | POWER&USB |     |     |
|     | VBUS_CC |         | COP10  P10        | VBUS      |     |     |     |     |     |     |             |     |     |     |      |     |                 |     |     |     |     |           |     |     |
|     |         | P I P 1 | 0 0 1   1 2 P I P | 1 0 0 2   |     |     |     |     |     |     |             |     |     |     |      |     |                 |     |     |     |     |           |     |     |
|     |         | P I P 1 | 0 0 3   3 4 P I P | 1 0 0 4   |     |     |     |     |     |     |             |     |     |     | GN D |     | C R O R2 2 55   |     |     |     |     |           |     |     |
P I P 1 0 0 5   5 6 P I P 1 0 0 6   COL1  1 V 2 P I R 2 5 0 2   P N I R 2 5 C 0 1   ( 0 Ω ) V D D _1.2A
|     |     |     |     |     |     |     | VBU S _ | C C |     |     | L1  | V B U S |     |     | P I R 2 8 0 2   |     | C RO R 22 6 6  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------- | --- | --- | --------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
A GND HEADER 3x2 GND P I C 1 0 2   P I C 2 0 2   C O C 7   P I L101  PIL10P 2I C 4 0 1     P I R 3 0 2   5 V 1 V 2 P I R 2 6 0 2   P N I R 2 6 C 0 1   ( 0 Ω ) VD D K COP2  P2 GND VBUS_USB A
|     |     |     |     |     |     |     | CO C C1 1                  |   COC2  C 2                |                                             | C7 NC(4                 | .7 u H /5 A )C4 C OC4  | COR3  R3                          |     |     | CR OR22 88                 |         |     |       | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | -------------------------- | ------------------------------------------- | ----------------------- | ---------------------- | --------------------------------- | --- | --- | -------------------------- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | NC(22uF/35 P I C 1 0 1   V | ) P I C 2 0 1   N C(0.1uF) | 0 PIU1010 PIU109 PIU108 PIU107 PPIU1I06 C70 | 1   PIC70 NC(100nF) 2   | P I C 4 0 2            | PIC3202 COC32   PIC330 2 COC 33   |     |     | P I R 2 8 0 1   N C (200k) | CUOU33  |     | G N D | 1   |     |     |     |     |     |
1 9 8 7 6 C U1 O U 1   N C ( 6F8 pB F) NC(15K P I R 3 0 1   ) C32 C33 V B U S PIP201  2 USBHS_DM COP4  P4 0
COP1  P1 P I R 4 0 2   PIC3201  PIC3301  NC(22uF) CC OC 556 6 P  I C 5 6 0 2   P I R 2 7 0 2   C R O R 2 2 7 7  D n P I P 3 2 0 2 USBHS_DP
B12B9 A1A4 G N D A 1 VBUS_CC GND N I N I W S W S T S COR4  RN4C(22uF) P I C 5 6 0 1   N C ( 0 Ω ) 1 6 C CO C88  G N D D p P I P 4 2 0 3   GND DNG GND 4
V B U S P I P A 1 4 0 A 1   V V B P I R 4 0 1   NC(4.7K) NC(4.7 p F ) P I R 2 7 0 1   1V 2 P I U 3 32 0 1   N C. F B P I5 U 3 0 6   3 V 3 1 0 u F S S R X - P I P 5 2 0 4   USBSS_RXP U D + P I 3 P 4 0 4   OTG_FS_DP
R F U 1 P P I I P P B 1 1 8 0 0 A B 4 8     C R OR 1  1 CL O L22  G N D P I U 3 0 2   G N D LDO _3 V 3 P I 4 U 3 0 5   P I C 8 0 2   PI C8 01   GND S S R X + P P I I P P 6 2 2 0 0 5 6     U SB S S _ RX N U D - P P I I 2 P P 4 4 0 0 2 3     OTG_FS_DM
COR13  R13 C C P I P A 1 5 0 A 5 C   C 1 PIR10 _ 1 2   PIR101  0Ω CC1 D P PIC5702   ICC O L C 552 7 7 0 2   P)IL20P 1 I U 3 0 3   S W V I N 5P I U 3 0 4 PIC5302 C  COC55 33  PIC5402  CCOC 55 45 4  V G N D P I P 7 2 0CO 7C1  1  DNG +5V P I 1 P 4 0 1
CC2 PIR1301  PIR1302  D - P I P B 1 7 0 B 7 O   T G _ FS _ DM D N I . . N N C(2 .2 uH S S T X - P I P 8 2 0 COP C1 8 CI 1C  21 1  1 0 1   P I 0 C 1 .1 1 0 2 u   F U SBSS_TXP
N C (5.1K) D + P I P A 1 6 0 A 6 O   T G _ F S _ D P N G V A C N C N B F G A GNDGNDGND PIC5701 NC(10uF) PIC5301 1uFPIC5401 10uF S S T X + P I P 9 2 0 C12 P 9 I C  1 2 0 1   P I 0.1uFUSBSS_TXN C 1 2 0 2   PIP400  VBUS_FS
CC1 COR12  R1 2 D - PIP10A7  B A 6 7 O O T T G G _ _ F F S S _ _ D D M P PIU100 PIU101 PIU102 PIU103 PIU104 PIU105  NC(CH2024Q) CH2003V G N D PIP200  0 0
PIR1201  NC(5.1K) PIR1202  D + PIP10B6  A 8 0 1 2 3 4 5 USB3.0-A
|     |     |       | R F U 1 PIP10A8  B 5       | CC1_2R9 COR9  | 0Ω CC2  |     |     |     |            |     |     |     |     |     | GND |     | GND |     | GND |     |     |     |     |     |
| --- | --- | ----- | -------------------------- | ------------- | ------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | A9A12 | C C P I P B 1 4 0          | B 5   PIR902  | PIR901  |     |     |     | VBUS_CC BF |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     |     |       | B4B1 V B U S P I P B 1 1 0 | B 4           |         |     |     |     |            |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     |     |       | G N D PIP10B1              | VBUS_CC       |         |     |     |     |            |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
TYPE-C
MCU
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | GND                | GNGDND                              |     |     |     |     |     | COR2  R2 0Ω            |       |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ----------------------------------- | --- | --- | --- | --- | --- | ---------------------- | ----- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | PD_SF_GTO          | MD_SF_GTO                           |     |     |     |     | 3V3 | PIR202  PIR201         | VDDIO |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | PIC1C701 OC17  C17 | COCP1IC19902  PIC2C102 OC21  C19C21 |     |     |     |     |     | COR5  R5 0Ω            |       |     |     |
| B   |     |     |     |     |     |     |     |     |     |     |     |     |     |                    |                                     |     |     |     |     |     | PIR502  COR10  PIR501  | VDD33 |     | B   |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | PIC1702  0.1uF     | 0.1uF PIC1901 PIC2101  0.1uF        |     |     |     |     |     | R100Ω                  |       |     |     |
PI R 4 RO50 2 44  P IR 4 5 0 1  P IRCR 4 O6 0R 2 4 4 66  N C P IR 4 ( 6 0 0 1  Ω ) 33DDV 8.1_OIV KDDV PIR100 2   P I R100 1   VDD33A
VBUS_USB CU O U 5 C  R 55  N C ( 0 Ω ) VBUS_FS CUO U6 6  V B U S 1DP 0DP 21CP 11CP 01CP 51AP 41AP 31AP 21AP 11AP 01AP 9AP 9CP 8CP 7CP 6CP 2FP 1FP 0FP C O R1 1
5 U2 V B U S U2 P I C 5 8 0 1   VDDIO PI R 110 R11NC(0Ω)VIO_1.8 2   P I R1101
|     |     | 3               | V O - P I 5 0 2 |   P I C 3 8 0 1   |     | 36 V I    | + V O - P I 6 0 2   |                             |     |     |     |     | PIU2066 PIU2065 PIU2064 PIU2063 PIU2062 PIU2061 PIU2060 PIU2059 PIU2058 PIU2057 PIU2056 PIU2055 PIU2054 PIU2053 PIU2052 PIU2051 PIU2050 PIU2049 PIU2048 PIU2047 PIU2046 PIU2045  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --------------- | --------------- | ----------------- | --- | --------- | ------------------- | --------------------------- | --- | --- | --- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | PIU 503   V I + | 15              |                   |     | PIU 0 3   | G N D 1             | P I C 5 8 0 2   CO C 558 8  |     |     |     |     |                                                                                                                                                                                  |     |     |     |     |     |     |     |     |     |     |     |
G N D P I U 0 1   P I C 3 8 0 2  C C OC 338 8  P I U 6 0 1   C 66 5 6 4 6 3 6 2 6 1 6 06 95 85 7 5 6 5 5 5 4 5 35 2 5 1 5 05 94 84 74 6 4 5 4 COU2
|     |     | C H 2 1 | 3   | 1 0 u F |     | C H 2 | 1 3 | 1 0 u F |     |     |     |     |             |                             |                                              |     | U2 CH32H417MEU6 |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | ------- | --- | ----- | --- | ------- | --- | --- | --- | --- | ----------- | --------------------------- | -------------------------------------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |         |     |         |     |       |     |         |     |     |     |     | 1DP 0 D 2 1 | 1 1 0 1 5 1 41AP 33DDV 31AP | P M D S U 9CP 8 C 7 C 6CP 81OIV KDDV 2FP 1 F | 0 F |                 |     |     |     |     |     |     |     |
|     |     |         |     |         |     |       | GND |         |     |     |     |     | P C P       | C P C P A P                 | D _ D _ I _ G B P P P                        | P   |                 |     |     |     |     |     |     |     |
|     |     |         |     | GND     |     |       |     |         |     |     |     |     |             |                             | G T G T T O V _                              |     |                 |     |     |     |     |     | LED |     |
O / 2 O / 0 G T
1 A / 1 1 1 A O /
P A P P 9 A
|     |     |     |     |     |     |     |     |     |     |     |     |                    |     |     | P   |       |                     |     |     |       |                                     | COLED1  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | ----- | ------------------- | --- | --- | ----- | ----------------------------------- | ------- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     | PD2 | PIU2067  6 7 P D 2 |     |     |     | PD15  | PIU2044  44 PD15    |     |     |       | COR16  R16                          | LED1    |     |     |
|     |     |     |     |     |     |     |     |     |     |     | PD3 | PIU2068  6 8 P D 3 |     |     |     | P D 1 | 4 PIU2043  4 3 PD14 |     |     | VDDIO | PIR1601  PIR1602 PILED101 PILED102  | LED1    |     |     |
|     |     |     |     |     |     |     |     |     |     |     | PD4 | PIU2069  6 9 P D 4 |     |     |     | P D 1 | 3 PIU2042  4 2 PD13 |     |     |       | 1k                                  |         |     |     |
|     |     |     |     |     |     |     |     |     |     |     | PD5 | PIU2070  7 0 P D 5 |     |     |     | P D 1 | 2 PIU2041  4 1 PD12 |     |     |       |                                     |         |     |     |
KEY RST XTAL PD6 PD7 P I U 2 7 7 0 2 1 7 1   P D 6 P D 1 1 P I U 3 4 2 9 0 0 4 0   PD11 PD10 C LED2 OLE D 2
COC23  C23 PF3 P I U 2 7 0 3 7 2   P D 7 P D 1 0 P I U 38 2 0 3 9   PB14 COC50 C50   10uF C R18 O R18  LED2
YEK TSRN COS1  S1 XI PF4 P I U 2 74 0 7 3   P F 3 PB14 P I U 37 2 0 3 8   PB13 PI C5001 PIC5002  VDDIO PIR18 01   PIR1802 PILED201   P I L ED202
1 2 PIC2301 PIC2302  PIY201  PF5 PIU2074  7 5 PF4 PB13 PIU2037  36 PB12 GND 1k
COS2  S2 PIS101  PIS102  18pF 1 PE0 PIU2075  7 6 P F 5 PB12 PIU2036  35 VDDIO CPIOCC262061  PIC2602  C260.1uF
1 2 4 3 PIY203  COY2  Y2 PE1 P I U 2 7 0 7 7 6   P P E E 0 1 VDDIO VIO18 P I U 34 2 0 3 5   VIO_1.8 GND
C 3V3R17 COR17  PIS201  PIS202  PIS104 RESET   PIS103  COC25  C25 25M COC30  C30 PF14 P I U 2 78 0 7 7   PF14 PB11 P I U 33 2 0 3 4   PB11 COC27PI C2701 PIC2702  C27 0.1uF C
4 3 CO C31 C31  3 PIR3002  XO VIO_1.8 P I U 2 79 0 7 8   VIO18 PB10 P I U 32 2 0 3 3   PB10 COC29PI C2901 PIC2902
PIR1702  10K PIR1701  PIS204  USER PIS203  PIC3102 PIC3101  PIC2501 PIC2502  COR30  PIC3001 PIC3002  PB3 CC1 PIU2079  PIU2080  8 0 P B 3 / C C 1 PE15 PIU2032  PIU2031  31 PE15 C29 2.2uF
|     |     |     |     |     |     |     | 18pF | R30 |     | 0.1uF | PB4 CC2 | PIU2081  8 1 P B 4 / C C 2 |     |     |     | P E 1 4 | PIU2030  3 0 PE14 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ----- | ------- | -------------------------- | --- | --- | --- | ------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
GND 0.1uF GND PIR3001  100k(NC) GND PB8 USBHS_DP PIU2082  8 2 P B 8 / U S B 2 D P /S W C L K P E 1 3 PIU2029  2 9 PE13
|     |     |     |     |     |     | GND |     | GND |     |     | PB9 USBSS_TXN USBHS_DM | PIU2083  8 8 4 3 P B 9 / U S B 2 | D M /S W D I O |     |     | P E 1 | 2 PIU2028  2 27 8 PE12 PE11 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | -------------------------------- | -------------- | --- | --- | ----- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     | USBSS_TXP              | PIU2084  8 5 S S T X N           |                |     |     | PE11  | PIU2027  2 6 PE10           |     |     |     |     |     |     |     |
VDD_1.2A PIU2085  8 6 S S T X P 0P_3PO/2CDASH/21CDA/2CP 0N_3PO/3CDASH/31CDA/3CP P E 10 PIU2026  2 5 PB1 If VIO18 is below 1.8V, the Ethernet port indicator circuit needs to be revised. ETH
COP6  P6 USBSS_RXN P I U 2 8 0 7 8 6   V D D 1 2A PB1/ADC9/CMP_N0/OP1 _ N 0 P I U 2 2 4 0 2 5   PB0 T h e  E t h e rn e t  p o r t  L E D  c a n no t  w o rk .
3V3 3V3 COP5  P5 PIN COC35 PIC3502  C35 PIC3C602 OC36  C36 USBSS_RXP P I U 2 8 0 8 8 7   S S R X N PB 0 /A D C 8 /O P 1 _ P 0 /C M P _ P 0 P I U 2 2 3 0 2 4   PA5 To   p re v e n t  c u rr e n t  b a ck f lo w ,d o  n o t p opulate resistor R21 and R22.
L E D PIP601  1 1 2 PIP602  GND 3V3 3V 3 PIU2088  S S R X P 0 C 1 C P A 5/ A D C 5/ O P 1 _ O 1 /D A C 2 PIU2023
|     | L E D PIP603  | 2 3 5 4 6 | PIP604  N R S T | G   | N D PIP501  1 3 | 4 2 PIP502  G N D |     |     |     | 2.2uF PIC3501  | PIC3601  0.1uF |     | P X N X | P X N X | D A D A 0O_3PO/0CDA/0AP |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --------- | --------------- | --- | --------------- | ----------------- | --- | --- | --- | -------------- | -------------- | --- | ------- | ------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P E 3 PIP605  7 8 PIP606  GND P D 7 PIP503  5 6 PIP504  P F 3 T _ T _ R _ R _ S H S COP7  P7 HR911105A
P E 4 PIP607  PIP609  9 1 0 PIP608  PIP6010  GND P D 6 PIP505  PIP507  7 8 PIP506  PIP508  P F 4 COP3  S E S E S E S E / 0 H / 1 COC37  J 8
P E 5 PIP6011  1 1 1 2 PIP6012  P B 0 P D 5 PIP509  9 1 0 PIP5010  P F 5 P3 D R D R D R D R 1 C 1 C A33DDV C 3 7 M D I R N PIP706  6 R D - J 7
P E 6 PIP6013  1 3 1 4 PIP6014  P B 1 P D 4 PIP5011  1 1 1 2 PIP5012  P D 3 3 V 3 PIP301  1 2 PIP302  G N D GND 33DDV E S E S E S E S KDDV N R P R N T P T 3 3 TS D A D A OIDDV G N D PIC3701 PIC3702  PIP705  5 J 6 R X -
P P C C 0 1 PIP6015  1 5 1 6 PIP6016  P P C B 1 2 0 P P D D 0 2 PIP5013  1 3 1 4 PIP5014  P P C D 1 1 2 G P B N 9 D PIP303  3 4 PIP304  G G N N D D SSV / 3 / 4 / 5 / 6 I D I D I D I D D D O RN / 0 / 1 4AP 0 . 1 u F M D I R P PIP703  3 R D + J 5
P C 3 P I P 6 0 1 7   1 7 1 8 P I P 6 0 1 8   P A 0 P C 1 1 P I P 5 0 1 5   1 5 1 6 P I P 5 0 1 6   P C 1 0 P B 8 P I P 3 0 5   5 6 P I P 3 0 6 G   N D E P E P E P E P M M M M V IX X C P C P COC39  C 3 9 M D I T N 2 T D - J 4
P A 4 P I P 6 0 1 9   1 9 2 0 P I P 6 0 2 0   P A 5 P D 1 4 P I P 5 0 1 7   1 7 1 8 P I P 5 0 1 8   P D 1 5 P I P 3 0 7   7 8 P I P 3 0 8   PIU200  PIU201 PIU202 PIU203 PIU204 PIU205 PIU206 PIU207 PIU208 PIU209 PIU2010 PIU2011 PIU2012 PIU2013 PIU2014 PIU2015 PIU2016 PIU2017 PIU2018 PIU2019 PIU2020 PIU2021 PIU2022  PIP702  4 J 3 R X +
P E 1 PIP6021  0 2 1 2 2 PIP6022  P E 1 1 P D 1 2 PIP5019  1 9 2 0 PIP5020  P D 1 3 0 1 2 3 4 5 6 7 8 9 0 1 1 1 21 3 1 4 1 5 1 6 1 71 81 91 02 12 22 G N D PIC3901 PIC3902  M D I T P PIP704  1 J 2 T X -
P E 1 PIP6023  2 2 3 2 4 PIP6024  P E 1 3 P D 1 0 PIP5021  2 1 2 2 PIP5022  P D 1 1 33DDV KDDV NRIDM PRIDM NTIDM PTIDM 33DDV TSRN 0CP 1CP 2CP 3CP OIDDV A33DDV 0 . 1 u F PIP701  T D + J 1 T X +
P E 1 PIP6025  4 2 5 2 6 PIP6026  P E 1 5 P B 1 3 PIP5023  2 3 2 4 PIP5024  P B 1 4 3EP 4EP 5EP 6EP IX OX 0AP 4AP 7
PIP6027  2 7 2 8 PIP6028  P B 1 1 PIP5025  2 2 5 7 2 2 6 8 PIP5026  P B 1 2 PIP707  N C 10 2 0 K 0 V pF 4X 7 5  o h ms
|     |     |          |     |     | PIP5027  | PIP5028  |           | COP11  P11 |       |     |     | GND |     |     |     |     |     |     | V D D | IO        | 8 G     | N D |     |     |
| --- | --- | -------- | --- | --- | -------- | -------- | --------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ------- | --- | --- | --- |
|     |     | COP8  P8 |     |     |          |          | V D D 3 3 | A 1 2      | 3 V 3 |     |     |     |     |     |     |     |     |     |       | CDOD1100  | PIP708  |     |     |     |
PF1 PIP801  1 2 PIP802  PF2 COP9  V D D 3 P P 3 I I P P 1 1 1 1 0 0 1 3     3 4 P P I I P P 1 1 1 1 0 0 2 4     3 V 3 PIC4C402 OC44  PIC4C502 OC45 PIC4C601 OC46  PIC4C701 OC47 PIC4C301 OC43  PIC4C902 OC49  PIC5C102 OC51  PID1001 PID1002  CO R P R I 211k 2 R 1 2   101  PIR2102  PIP709  9
D PC6 P I P 8 0 3   3 4 P I P 8 0 4   PC7 P9 V D D I P O I P 1 1 0 5   5 6 P I P 1 1 0 6   3 V 3 C44 C45 C46 C47 C43 C49 C51 ELED 1 PIP7010  1 0 D
PC8 P I P 8 0 5   5 6 P I P 8 0 6   PC9 3V3 PIP901  1 2 PIP902  3 V 3 V I O _ 1 P I .8 P 1 1 0 7   7 8 P I P 1 1 0 8   3 V 3 PIC4401  PIC4501  PIC4602  PIC4702  PIC4302  PIC4901  PIC5101  Diode COR22
PA9 PA11 PIP807  7 8 PIP808  PA10 PA12 GND PB9 PIP903  3 4 PIP904  G G N N D D G G N N D D PIP1109  9 1 0 PIP11010  G G N N D D 0.1uF 0.1uF 2.2uF 0.1uF 10uF 0.1uF 0.1uF E R L PIR2201  2 E 2 D0 1k PIR2202  PIP7012  1 1 2 1
PA13 PIP809  9 10 PIP8010  PA14 PB8 PIP905  5 6 PIP906  KEY G N D PIP11011  1 1 1 2 PIP11012  G N D PIP7011
|     | PA15 | PIP8011  1 1 | 1 2 PIP8012  VDD33 | PF0 | PIP907  7 | 8 PIP908  PF14 | V B U S PIP11013  _ | U SB 1 3 1 4 PIP11014  | G N D |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | ------------ | ------------------ | --- | --------- | -------------- | ------------------- | ---------------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
GND PIP8013  1 3 1 4 PIP8014  GND PE0 PIP909  9 1 0 PIP9010  PB3 V B U S PIP11015  _ C C 1 5 1 6 PIP11016  G N D GND GND GND GND GND PF0 COR23  R23ELED1
GND PIP8015  1 5 1 6 PIP8016  GND PE1 PIP9011  11 1 2 PIP9012  PB4 PIP11017  1 7 1 8 PIP11018  0Ω PIR2301  PIR2302
|     | 3V3 | PIP8017  1 7 | 1 8 PIP8018  3V3 |     | PIP9013  13 14 | PIP9014  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | ---------------- | --- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PIP8019  19 20 PIP8020
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | PF2 | COR24  R24ELED0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- |
PIR2401  0Ω PIR2402
|     |     | 1   |     |     |     | 2   |     |     | 3   |     |     | 4   |     |     | 5   |     | 6   |     |     | 7   |     |     | 8   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |         | 1   |              | 2    |     |     | 3           |     |     |     | 4        |     |     | 5                          |          |          | 6       |          | 7   |     |           | 8   |     |
| --- | ------- | --- | ------------ | ---- | --- | --- | ----------- | --- | --- | --- | -------- | --- | --- | -------------------------- | -------- | -------- | ------- | -------- | --- | --- | --------- | --- | --- |
|     |         |     |              |      |     |     | POWER&USBPD |     |     |     | GND      |     |     | C RO R225 5                |          |          | GND     |          |     |     |           |     |     |
|     |         |     |              |      |     |     |             |     |     |     |          |     |     | PINR25C01 (0Ω)             | VDD_1.2A | COP2  P2 |         | VBUS_USB |     |     | POWER&USB |     |     |
|     | VBUS_CC |     | COP10  P 1 0 | VBUS |     |     |             |     |     |     |          |     | 1V2 | PIR250 2                   |          |          | 0       |          |     |     |           |     |     |
|     |         |     |              |      |     |     |             |     |     |     | PIR2802  |     |     | C RO R226 6 PINR26C01 (0Ω) | VDDK     |          | G N D 1 |          |     |     |           |     |     |
PIP1001  1 3 2 4 PIP1002  1V2 PIR260 2   V B U D n S PIP201  2 USBHS_DM COP4  P4 0
P P I I P P 1 1 0 0 0 0 3 5     5 6 P P I I P P 1 1 0 0 0 0 4 6     P I R 2 8 0 1   C R O R 2 2 8 8   D p P P I I P P 3 2 2 0 0 2 3 USBHS_DP     DNG
|     |     |     |     |     |     |     | COL1  |     |     |     | N C ( 2 0 | 0 k ) | CUO U33   |     |     |     | G N D P I P 4 2 0 4   | GND | GND | P I P 4 4 0 4   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --------- | ----- | --------- | --- | --- | --- | --------------------- | --- | --- | --------------- | --- | --- | --- |
H E ADE R 3x2 VBU S _ C C L1 V B U S CCO C 556 6  P I C 5 6 0 2   P I R 2 7 0 2   S S R X - P I P 5 2 0 5   USBSS_RXP U D + P I P 3 4 0 3   OTG_FS_DP
GND GND P I C 1 0 2  CO C1   P I C 2 0 2  COC2  P I L101  PIL10P 2I   P I R 3 0 2   5V C R O R 2 2 7 7   S S R X + P I P 6 2 0 6   USBSS_RXN U D - P I P 2 4 0 2   OTG_FS_DM
C 1 C 2 C C7 O C 7   NC(4 .7 u H /5 A )C4 C 4 0 1   C OC4  COR3 P P I C 5 6 0 1   N C ( 0 Ω ) 10 6 C CO C88  G N D P I P 7 2 C 0 O 7 C 1   1   DNG +5V P I P 1 4 0 1
A NC(22uF/35 P I C 1 0 1   V ) P I C 2 0 1   N C(0.1uF) PIU1010 PIU109 PIU108 PIU107 PPIU1I06 C70 1   PIC70 NC(100nF) 2   P I C 4 0 2   R3 I C 1 7 0 2   P I C 5 0 2   NC(4.7 p F ) P I R 2 7 0 1   1V 2 CL O L 22   G N D P I U 3 2 1   N G N C. D LDO _3 F V B 3 P I5 U 3 0 6   3 V 3 1 0 u F GND S S T X - P I P 8 9 2 C 0 C11 C12 O P 8 C I 1 C   1 2 1   0 1   P I 0.1uFUSBSS_TXP 0.1uFUSBSS_TXN C 1 1 0 2   VBUS_FS A
C P1 OP 1  0 1 9 8 7 6 C U1 O U 1   N C ( 6F8 pB F) NC(15K P I R 3 0 1   ) COC17 C17   COC C5 5  PPIC5 702I C L 2 0 2   P IL201 P P  I I U U 3 3 3 0 0 2 3     S W V I N 5P P I I 4 U U 3 3 0 0 4 5 PIC5302 C    PIC5402 C P I C 5 80 V 2   PI C 80 1  S S T X + P I P 0 2 0 P 9 I C   1 2 0 1   P I C 1 2 0 2   PIP400
B12B9 A1A4 A 1 VBUS_CC P I R 4 0 2   P I C 1 7 0 1   P I C 5 0 1   NC(22uF) C O C 55 7  7 N C ( 2 .2 uH ) COC55 33  COC 55 4 4  G N D P I P 2 0 0   0
G N D P I P A 1 4 0 A 1   GND N I N I W W T S COR4  RN4C(22uF) PIC5701 NC(10uF) PIC5301 1uFPIC5401 10uF USB3.0-A
|     |              |                   | V B U S P I P B 1 8 0 A 4           |                            |                                            | V V S S B                 |     | NC(4.7K)  |     |     |     |     |         |     |     |     | GND |     |     |     |     |     |     |
| --- | ------------ | ----------------- | ----------------------------------- | -------------------------- | ------------------------------------------ | ------------------------- | --- | --------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | COR13        |                   | R F C U C 1 P I P A 1 5 0 B 8 C   C | 1 _ 1 CO R1 R1  0Ω CC1     |                                            |                           |     | PIR401    |     |     |     |     | CH2003V |     |     |     |     |     |     |     |     |     |     |
|     | CC2 R13      |                   | D - P I P B 1 7 0 A 5 O   T         | G PIR102 _ FS_DM   PIR101  |                                            | D                         |     |           |     |     | GND |     |         | GND |     |     |     |     |     |     |     |     |     |
|     | PIR1301  N   | C (5.1K) PIR1302  | D + PIP10B7  PIP10A6  A 6 O T       | G _ F S _ D P              | D                                          | N N                       |     |           |     |     |     |     |         |     |     |     |     |     |     |     |     |     |     |
|     | COR12  R1    | 2                 | D - PIP10A7  A 7 O T                | G _ F S _ D M              | N G                                        | I V A . C N . C N B F G A |     | GNDGNDGND |     |     |     |     |         |     |     |     |     |     |     |     |     |     |     |
|     | CC1 PIR1201  | PIR1202           | D + P I P B 1 6 0 B 6 O   T         | G _ F S _ D P              | PIU100 PIU101 PIU102 PIU103 PIU104 PIU105  |                           |     |           |     |     |     |     |         |     |     |     |     |     |     |     |     |     |     |
NC(5.1K) R F U 1 P I P A 1 8 0 A 8   COR9  R9 0 1 2 3 4 5 NC(CH2024Q) GND GND GNDGND MCU
|     |     |        | C C PIP10B5  B B 4 5 CC1_2       | PIR902  PIR901  0Ω CC2 |         |     |     |     |     |     |                                                                                                                                                                                                                                                                  |                                        |                              |                                     |                             |                |     |     |     |       |          |     |     |
| --- | --- | ------ | -------------------------------- | ---------------------- | ------- | --- | --- | --- | --- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------- | ----------------------------------- | --------------------------- | -------------- | --- | --- | --- | ----- | -------- | --- | --- |
|     |     | A9A12  | B4B1 V B U S P I P B 1 1 0 B 4   |                        | VBUS_CC | BF  |     |     |     |     |                                                                                                                                                                                                                                                                  | COC1PIC61602   C16 PD_SF_GTO MD_SF_GTO | COC18 PIC1802  C18           | PIC1C902 OC19 PIC2C002 OC20  C19C20 |                             |                |     |     |     |       |          |     |     |
|     |     |        | G N D P I P 1 0 B 1              | VBUS_CC                |         |     |     |     |     |     |                                                                                                                                                                                                                                                                  |                                        |                              |                                     |                             |                |     |     |     |       |          |     |     |
|     |     | TYPE-C |                                  |                        |         |     |     |     |     |     |                                                                                                                                                                                                                                                                  | 0.1uF PIC1601                          | 0.1uF PIC1801                | PIC1901  0.1uF0.1uF PIC2001         |                             |                |     |     |     |       |          |     |     |
|     |     |        |                                  |                        |         |     |     |     |     |     |                                                                                                                                                                                                                                                                  | 33DDV                                  | OIDDV                        | 8.1_OIV KDDV                        |                             |                |     |     |     |       |          |     |     |
|     |     |        |                                  |                        |         |     |     |     |     |     | 01CP 51AP                                                                                                                                                                                                                                                        | 41AP 31AP 21AP 11AP                    | 01AP 9AP 8AP 9CP 8CP 7CP 6CP | 2FP 1FP 0FP 51DP 41DP 31DP          | 21DP 11DP 01DP 9DP 8DP 51BP | 41BP 31BP 21BP |     |     |     | COR2  |          |     |     |
|     |     |        |                                  |                        |         |     |     |     |     |     | PIU2096 PIU2095 PIU2094 PIU2093 PIU2092 PIU2091 PIU2090 PIU2089 PIU2088 PIU2087 PIU2086 PIU2085 PIU2084 PIU2083 PIU2082 PIU2081 PIU2080 PIU2079 PIU2078 PIU2077 PIU2076 PIU2075 PIU2074 PIU2073 PIU2072 PIU2071 PIU2070 PIU2069 PIU2068 PIU2067 PIU2066 PIU2065  |                                        |                              |                                     |                             |                |     |     | 3V3 | R2    | 0Ω VDDIO |     |     |
P I R C4 RO5 R0 442 5  P IR 4 5 0 1   VBUS_FS CU OU 66  P I CR R 4O 6 R0 44 26  6  N P C I R 4 ( 6 0 0 1   Ω ) P I R 2 0 C R5 2 O R   5   P I R 2 0 1
VBUS_USB CO U U 5 5  5  N C ( 0 Ω ) V B U S V B U S 69 5 9 4 9 3 9 2 9 1 9 0 9 9 8 8 8 7 8 6 8 5 8 4 8 3 8 2 8 1 8 0 8 9 7 8 7 7 7 6 7 5 7 4 7 3 7 2 7 1 7 0 7 9 6 8 6 7 6 6 6 5 6 P I R 5 0 2   P I 0Ω R 5 0 1   VDD33
U2 V O - P I U2 6 0 2   P I C 5 8 0 1   U2 COU2  C R7 O R 7
3 V O - P I 5 0 2   P I C 3 8 0 1   PIU 63 0 3   V I + 01CP 5 4 3 3 3 P M D S 8 9 C 8 C 7 C 6 C O 8 K 2 F 1 F 0 5 4 3 1 2 1 1 0 9 D 8 D 5 4 3 1 2 CH32H417QEU6 P I R 7 0 2   P I 0Ω R 7 0 1   VREF
PIU5 03   V I + 15 P I C 3 8 0 2  C G N D P I U 16 0 1   P I C 5 8 0 2   CC OC 558  8 1 A 1 A D D 1 A P D _ D I _ G U B A P P P P P I D 1 O I D D P P F P 1 D 1 D D P 1 D D P 1 D P P 1 B P 1 B P B P 1 B P C R100Ω O R 1 0
G N D P I U 0 1   C OC 338  8 P P V G T _ G T V _ D V V V P P P P COC4 C43 3   10uF PI R 1 0 0 2   PI R 1 0 0 1   VDD33A
C H 2 1 3 1 0 u F C H 2 1 3 1 0 u F O / T O O / 0 G T P IC 4302 PIC4301  C O R 1 1
| B   |     |     |     |     |     |     |     |     |     |     |     | 2 1 A / 1 1 | 1 A O / |     |     |     |     | GND |     | R11NC(0Ω) | VIO_1.8 |     | B   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --------- | ------- | --- | --- |
GND GND PC11 9 7 P A P P 9 A 6 4 VDDIO C C260.1uF O C 2 6   VDDIO PIR1102  PIR1101
|     |     |     |     |     |     |     |     |     | PC12 | PIU2097  9 8 P P C C1        | 1 1 2 |     | P   |     |     |     | V V D I D O I 1 O 8 PIU2064  6 3 | VIO_1.8 PI C 2 6 0 1  PIC260C2 OC27  C270.1uF GND |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------------------------- | ----- | --- | --- | --- | --- | --- | -------------------------------- | ------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | PD0  | PIU2098  9 9 P D             | 0     |     |     |     |     |     | P B 1 1 PIU2063  6 2             | PB11 PIC2701 PIC2702                              |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     | PD1  | PIU2099  PIU20100  1 0 0 P D | 1     |     |     |     |     |     | P B 1 0 PIU2062  PIU2061  6 1    | PB10 CPIOCC292092  PIC2901                        |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     | PD2  | PIU20101  1 0 1 P D          | 2     |     |     |     |     |     | P E 1 5 PIU2060  6 0             | PE15 C292.2uF                                     |     |     |     |     |     |
IK23X COC23  XTAL PD3 PIU20102  1 0 2 P D 3 P E 1 4 PIU2059  5 9 PE14
|     |     |     |     |     | C23 |     |     | C O C30 |   PD4 | P I U 1 2 0 0 3 1 0 3   P D | 4   |     |     |     |     |     | P E 1 3 P I U 5 2 8 0 5 8   | PE13 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --------------------------- | --- | --- | --- | --- | --- | --- | --------------------------- | ---- | --- | --- | --- | --- | --- |
C C22 O C22   C R14 O R14  PC14 PIC2301 PIC2302  PIY201  XI C30 VIO_1.8 PD5 P I U 1 1 2 0 0 0 4 5 1 0 4   P D 5 P E 1 2 P I U 5 5 2 7 6 0 5 7   PE12 PE11 LED
GND PIC22 02   PI C2201  PIY101  PIR140 2   NC(0Ω) PIR1401  18pF 1 PIC30 02   PI C3001  PD6 P I U 1 2 0 0 6 1 0 5   V IO 18 @VDD33 power P E 1 1 P I U 5 2 5 0 5 6   PE10 COLED1  LED1
12pF 1 GND COY2  Y2 0.1uF PD7 P I U 107 2 0 1 0 6   PD 6 P E 1 0 P I U 54 2 0 5 5   PE9 COR16  R16 LED1
COY1  Y1 C C25 OC2 5   P I Y 2 0 3   25M GND PF3 P I U 1 2 0 0 8 1 0 7   PD7 @V D D I O  p o w e r PE9/OP2_P0 P I U 5 2 3 0 5 4   PE8 VDDIO PIR1601  PIR1602 PILED101 PILED102
COC24  C24 PIY102  32.768 COR15  k 3 XO PF4 P I U 1 2 0 0 9 1 0 8   P F 3 P E 8 / O P 2 _ N 0 P I U 5 2 2 0 5 3   PE7 1k
2 R 15 PC15 PIC250 1  P I C2502  PI R 3 0 0 2   PF5 P I U 1 2 1 0 0 1 0 9   P F 4 @ V IO 1 8  p o w e r P E 7 / O P 2 _ O 0 P I U 5 2 1 0 5 2   VDDIO
PIC2402 PIC2401  OK23X PIR1502  NC(0Ω) PIR1501  18pF COR30  R 3 0 PE0 P I U 1 2 1 0 1 1 1 0   P P E F5 0 V D P D F I 1 O 3 P I U 5 2 0 0 5 1   PF13 PCICO3C23021  PIC3202  C320.1uF GND COR18  COLED2  LED2
12pF PIR3001  10 0 K(NC) PE1 P I U 1 2 1 0 2 1 1 1   P E 1 @ V D D 1 2   po w e r PF12/OP2_N1 P I U 49 2 0 5 0   PF12 VDDIO R18 LED2
GND COC33  C33 PF14 PIU20112  PIU20113  1 1 3 P F 1 4 P F 1 1 /O P 2 _ P 1 PIU2049  PIU2048  4 8 PF11 PIR1801  1k PIR1802 PILED201 PILED202
|     |     |     |     |     |     |     |     | GND PIC3301 PIC3302  | VDDIO | PIU20114  1 1 4 V D     | D IO    |     | @ V | D D 3 3 & V B A T power |                      | P B | 2 / C M P _ P 1 PIU2047  4 7 | PB2 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ----- | ----------------------- | ------- | --- | --- | ----------------------- | -------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |                      | PB3   | CC1 PIU20115  1 1 5 P B | 3 /C C1 |     |     |                         | PB1/ADC9/OP1_N0/OP2_ | O 1 | / C M P _ N 0 PIU2046  4 6   | PB1 |     |     |     |     |     |
KEY RST 0.1uF PB4 CC2 PIU20116  116 PB4/CC2 PB0/ADC8/OP1_P0/CMP_P0 PIU2045  45 PB0 ETH
3V3 NRST 1 2 PB5 PB6 PIU20117  1 1 1 1 8 7 P B 5 PC5/ADC15 PIU2044  43 44 PC5 PC4
|     |     |     |     |     | PIS10C1OS 1  1 | 2 PIS102  |     |     | PB7 | P I U 1 2 1 0 9 1 1 8   P B | 6   |     |     |     | PC4/ADC14/OP1_O0/CMP_N1 |     | P I U 4 2 2 0 4 3   | PA7 |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | ----------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
PIR1701  S1 RESET PB8 USBHS_DP P I U 1 2 2 0 0 1 1 9   P B 7 P A 7 / A D C 7 / O P 1 _ N 1 P I U 4 2 1 0 4 2   PA6
COR R17 1 7  PB9 USBHS_DM P I U 1 2 2 0 1 1 2 0   P B 8 / U S B 2 D P /S W C L K P A 6 / A D C 6 / O P 1 _ P 1 P I U 4 2 0 0 4 1   PA5 I f  V I O 1 8  i s   b e l o w   1 .8 V ,   t h e  E t h e r n e t  p o r t  i n d i c a t o r   c i r cu i t  n e e d s  t o  be revised.
10K C C31 O C31   P I U 122 2 0 1 2 1   P B 9 / U S B 2 D M /S W D I O P A 5 / A D C 5 / O P 1 _ O 1 / D A C 2 P I U 3 2 9 0 4 0   PA4 T h e  E t h e r n e t  p o r t  L E D   c a n n o t   w o r k .
KEY PIR1702  1 1 2 2 GND GND GND USBSS_TXN P I U 1 2 2 0 3 1 2 2   VSS S S T X N P 0 A 4 / A D C 4 / O P 3 _ O 1 V / D D A D C I O 1 P I U 3 2 8 0 3 9   VDDIO GND T o   p r e v e n t   c u r r e n t  b a c k f l o w ,d o  n o t  p o p u l a t e  r e s i s t o r   R 2 1  a n d   R 2 2 .
C P I S20C1OS 2  S2 PIS202  PIC310 2   PI C3101  USBSS_TXP P I U 1 2 2 0 4 1 2 3   S S T X P 0 P _ N _ P A 3 / A D C 3 / O P 3 _ N 1 P I U 3 2 7 0 3 8   PA3 PCICO3C43042  PIC3401  C340.1uF C
USER 0.1uF VDD_1.2A P I U 1 2 2 0 5 1 2 4   V D D 1 2A 3 P 3 P PA2/ADC2/OP3_P1 P I U 36 2 0 3 7   PA2
COP6  COC35 PIC3502  PIC3C602 OC36  USBSS_RXN PIU20125  PIU20126  1 2 6 S S R X N O / O / PA1/ADC1 PIU2036  PIU2035  35 PA1 COP7
P6 PIN C35 C36 USBSS_RXP PIU20127  1 2 7 S S R X P NXT_SEDRES/4EP NXR_SEDRES/6EP 0 C D 1 C 2 C D 3 C D PA0/ADC0/OP3_O0 PIU2034  34 PA0 P7 HR911105A
3V3 PIP601  1 2 PIP602  3V3 PIC3501  PIC3601  VDD33 PIU20128  1 2 8 V D D 3 3 PXT_SEDRES/3 PXR_SEDRES/5EP A D A A A VDD33A PIU2033  33 VDD33A PIC5102 PIC5101  GND COC37  J 8
P P F F 0 2 PIP603  3 4 PIP604  P G F N 1 D 2.2uF 0.1uF 4CDASH/8FP 5C 6C S H S H S H S H COC51  C510.1uF C 3 7 M D I R N PIP706  6 5 R D - J 7
P B 1 PIP605  5 5 6 PIP606  N R S T D D / 0 1 / 1 1 / 2 1 / 3 1 G N D PIC3701 PIC3702  M D I R P PIP705  3 J 6 R X -
P B 1 PIP607  3 7 8 PIP608  P B 1 4 PIC4C102 OC41  C41 N A A S C D C D C D C D 0 . 1 u F PIP703  R D + J 5
P B 1 P 1 I P 6 0 9   9 1 0 P I P 6 0 1 0   P B 1 2 COP5  P5 COP9  P9 GND OIDDV TABV 3 4 5 K D R P R NTIDM PTIDM 33DDV S H H /0 T A A A A O ID A PF COC39  C 3 9 M D I T N 2 T D - J 4
P E 1 PI 5 P 6 0 1 1   1 1 1 2 P I P 6 0 1 2   P B 1 0 GND K E Y VR E F 3 V 3 PIC4101  0.1uF SSV 2 E E 1 C 1 C 1 C D I D M I D M 6FP 7FP /9 F 1 F SSV I O S R / 0 C / 1 C / 2 C / 3 C D S SV E R PIP702  4 J 3 R X +
P E 1 PIP6013  3 1 3 1 4 PIP6014  P E 1 4 P B 7 PIP501  1 2 PIP502  P B 6 V D D 3 PIP901  3 A 1 2 PIP902  3 V 3 PIU200  P PIU201 PIU202 PIU203 PIU204 PIU205 PIU206 PIU207 PIU208 PIU209 PIU2010 PIU2011 PIU2012 PIU2013 PIU2014 PIU2015 PIU2016 PIU2017 PIU2018 PIU2019 PIU2020 PIU2021 PIU2022 PIU2023 PIU2024 PIU2025 PIU2026 PIU2027 PIU2028 PIU2029 PIU2030 PIU2031 PIU2032  P P P P V P P X X N P P P P V V G N D PIC3901 PIC3902  M D I T P PIP704  1 J 2 T X -
P E 1 PIP6015  1 1 1 5 7 1 1 6 8 PIP6016  P E 1 2 P B 5 PIP503  3 5 4 6 PIP504  P B 4 V D D 3 PIP903  3 3 5 4 6 PIP904  3 V 3 0 . 1 u F PIP701  T D + J 1 T X +
P E 9 PIP6017  1 9 2 0 PIP6018  P E 1 0 P F 1 PIP505  4 7 8 PIP506  P B 3 V D D I PIP905  O 7 8 PIP906  3 V 3 0 1 2 3 4 5 6 7 8 9 0 1 1 1 2 1 3 1 41 51 61 71 81 91 0 2 1 2 22 3 2 4 2 5 2 6 2 7 2 8 2 9 2 0 3 1 3 2 3 7 N C 10 0 0 pF
P E 7 PIP6019  PIP6021  2 1 2 2 PIP6020  PIP6022  P E 8 P E 0 PIP507  PIP509  9 1 0 PIP508  PIP5010  P E 1 V I O _ 1 PIP907  PIP909  .8 9 1 0 PIP908  PIP9010  3 V 3 GND OIDDV TABV IK23X OK23X KDDV NRIDM PRIDM NTIDM PTIDM 33DDV TSRN OIDDV FERV PIP707  2 K V 4X 7 5  o h ms
P F 1 PIP6023  2 2 3 2 4 PIP6024  P F 1 3 P F 5 PIP5011  1 1 1 2 PIP5012  P F 4 V B A T PIP9011  1 1 1 2 PIP9012  3 V 3 2EP 3EP 4EP 5EP 6EP 31CP 6FP 7FP 8FP 9FP 01FP OX 0CP 1CP 2CP 3CP DNG VDDIO CDOD1100  PIP708  8 G N D
|     | P B 2 PIP6025  | 2 5 2 6 PIP6026  | P F 1 1 | P F 3 PIP5013  1 3 1 4 PIP5014  P D 7 | G N D PIP9013  | 1 3 1 4 PIP9014  | G N D |     |     |     |     |     |     | IX  |     |     |     |     |     |     |     |     |     |
| --- | -------------- | ---------------- | ------- | ------------------------------------- | -------------- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P B 0 PIP6027  2 7 2 8 PIP6028  P B 1 P P D D 4 6 PIP5015  1 5 1 6 PIP5016  P P D D 3 5 V V B B U U S S PIP9015  _ _ C U C SB 1 5 1 6 PIP9016  G G N N D D GND PID1001 PID1002  E L E D COR21  R PIR2101  1 211 k PIR2102  PIP709  1 9 0
PD2 P I P 5 0 1 7   1 7 1 8 P I P 5 0 1 8   PD1 PIP9017  1 7 1 8 PIP9018  PIP7010
COP8  P8 PC12 P I P 5 0 1 9   19 20 P I P 5 0 2 0   PD0 PIC4C402 OC44 PIC4702 COC47 PIC4C502 OC45 PIC4C601 OC46  C44 C47 C45 C46 PIC4C202 OC42 PIC4C002 OC40  C42 C40 GND COC48 PIC4801  C48 PIC4C902 OC49  C49 Diode COR22  R22 1k 12
G N D P C 5 P C 1 PIP5021  0 21 22 PIP5022  P C 1 1 ELED0 PIR2201  PIR2202  PIP7012  11
P A 7 PIP801  1 2 PIP802  P C 4 P A 1 PIP5023  4 23 24 PIP5024  P A 1 5 PIC4401  0.1uF PIC4701  0.1uF PIC4501  0.1uF PIC4602  2.2uF PIC4201  0.1uF PIC4001  10uF 0.1uF PIC4802  PIC4901  0.1uF PIP7011
|     | P A 5 PIP803  | 3 4 PIP804  P | A 6 | P A 1 PIP5025  2 25 26 PIP5026  P A 1 | 3   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | ------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P A 3 PIP805  5 7 6 8 PIP806  P A 4 P A 1 PIP5027  1 27 29 30 28 PIP5028  P A 1 0 P F 0 COR23  R 2 3 E L E D 1
P A 1 PIP807  9 1 0 PIP808  P A 2 P A 8 PIP5029  31 32 PIP5030  P A 9 GND GND GND GND GND GND 0Ω PIR2301  PIR2302
|     | P C 3 PIP809  | 1 1 1 2 PIP8010  P | A 0 | P C 8 PIP5031  33 34 PIP5032  P C 9 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | ------------------ | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P C 1 PIP8011  PIP8013  1 3 1 4 PIP8012  PIP8014  P C 2 P C 6 PIP5033  PIP5035  3 5 3 6 PIP5034  PIP5036  P C 7 COP3  P3 COR24
D P F 1 0 PIP8015  1 5 1 6 PIP8016  P C 0 P D 1 PIP5037  4 3 7 3 8 PIP5038  P D 1 5 3 V 3 PIP301  1 2 PIP302  G N D P F 2 PIR2401  PIR2402  R 2 4 E L E D 0 D
P F 8 PIP8017  1 7 1 8 PIP8018  P F 9 P D 1 PIP5039  2 3 9 4 0 PIP5040  P D 1 3 G N D PIP303  3 4 PIP304  G N D 0Ω
|     | P P C F 6 1 4 PIP8019  | 1 9 2 0 PIP8020  P P   | C F 7 1 5 | P P D D 1 8 PIP5041  0 4 1 4 2 PIP5042  P P D D 1 9 | 1 P P B B 8 9 PIP305  | 5 6 PIP306  | G G N N D D |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------- | ---------------------- | --------- | --------------------------------------------------- | --------------------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | P E 6 PIP8021          | 2 1 2 2 PIP8022  P     | C 1 3     | PIP5043  4 3 4 4 PIP5044                            | PIP307                | 7 8 PIP308  |             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | P E 4 PIP8023          | 2 3 2 4 PIP8024  P     | E 5       |                                                     |                       |             |             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | P E 2 PIP8025          | 2 5 2 6 PIP8026  P     | E 3       |                                                     |                       |             |             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | L E D 1 PIP8027        | 2 7 2 8 PIP8028  L     | E D 2     |                                                     |                       |             |             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | G N D PIP8029          | 2 9 3 0 PIP8030  G     | N D       |                                                     |                       |             |             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | 3V3 PIP8031            | 3 33 1 34 3 2 PIP8032  | 3V3       |                                                     |                       |             |             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | PIP8033                | PIP8034                |           |                                                     |                       |             |             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     |                        | 1                      |           | 2                                                   |                       |             | 3           |     |     |     | 4   |     |     | 5   |     |     | 6   |     | 7   |     |     | 8   |     |

|     |     | 1   |     | 2   |     | 3   |     |     | 4   |     |     | 5   |     |     | 6   |     |     | 7   |     |     | 8   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
POWER&USB
|     |     |     |               |     |     |     |     |     | COP2  | GND      |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | C O R R 1 1   |     |     |     |     |     | P2    | VBUS_USB |     |     |     |     |     |     |     |     |     |     |     |     |
1 V 2 P I R 1 0 C2 R  P I N R 1 0 C 1   ( 0 Ω ) V D D _1.2A G N D 0 0 P ICR 4O 6R0 426  P I R 4 6 01
O R 3 3   V B U S P I P 1 2 0 1   COP4  P4 P I R RC4O5 R0 442 5  5  P IR 4 50 1  VBUS_USB C OU 66  R 4 6  N C ( 0 Ω )
1 V 2 P I R 3 0 2   P I N R 3 0 C 1   ( 0 Ω ) VD D K D n P I P 2 2 0 2 USBHS_DM   DNG VBUS_HS CU O U 5 5  N C ( 0 Ω ) V B U S U V B U S
A D p P I P 3 4 2 0 3 USBHS_DP   GND P I 4 3 P 4 0 4 U   S B H S _ D P U2 P I C 3 8 0 1   V O - P I U2 6 0 2   P I C 5 8 0 1   A
|     |     |     |     |     |     |     |     |     | G N D   | P I P 5 2 0 4   USBSS_RXP   | GND |     | U D + P I 2 P 4 0 3 U     | S B H S _ D M |     | PIU3503 V I + V O | - P I 5 0 2                       |           | PIU 3 6 | 0 3   V I +           |                               |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------------------- | --- | --- | ------------------------- | ------------- | --- | ----------------- | --------------------------------- | --------- | ------- | --------------------- | ----------------------------- | --- |
|     |     |     |     |     |     |     |     |     | S S R X | - P I P 6 2 0 5   USBSS_RXN |     |     | DNG U D - P I 1 P 4 0 2   |               |     |   G N             | D P I U 15 0 1   P I C 3 8 0 2  C | OC 338 8  |         | G N D P I U 1 6 0 1   | P I C 5 8 0 2   CC O C 558 8  |     |
GN D S S R X + P I P 7 2 0 6   +5V P I P 4 0 1   C C H 2 1 3 1 0 u F
|     |     |            |         |     |     |     |     |     | G N D             | P I P 8 2 0 C11 C O 7 C 1   1   0.1uFUSBSS_TXP                    |     |     | PIP400  VBUS_HS |     |     | C H 2 1 3 | 1   | 0 u F |     |     |     |     |
| --- | --- | ---------- | ------- | --- | --- | --- | --- | --- | ----------------- | ----------------------------------------------------------------- | --- | --- | --------------- | --- | --- | --------- | --- | ----- | --- | --- | --- | --- |
|     |     | PIR602     |         |     |     |     |     |     | S S S S T T X X + | - P I P 9 2 0 C12 C O P8 IC C1   12 1  01 PIC1102  0.1uFUSBSS_TXN |     |     |                 |     |     |           |     |       |     |     |     |     |
|     |     |            |         |     |     |     |     |     | G N D             | P I P 0 2 0P 9IC  1201 PIC1202                                    |     |     | 0               |     |     |           | GND |       |     | GND |     |     |
|     |     | CR OR66    |         |     |     |     |     |     |                   | P I P 2 0 0                                                       |     |     |                 |     |     |           |     |       |     |     |     |     |
|     |     | PIR601     |         |     |     |     |     |     | USB3.0-A          |                                                                   |     |     |                 |     |     |           |     |       |     |     |     |     |
|     |     | N C (200k) | CUOU11  |     |     |     |     |     |                   | GND                                                               |     |     |                 |     |     |           |     |       |     |     |     |     |
CCOC77 PIC702  PIR402 CROR44
N C (0 Ω )
|     | NC(4.7pF)PIC701  |                             | 1 N C.                                  | F B 6                             | C CO C8 8  1 0 u F                       |     |     |     |     |     |     |     |     |     |     |     |     |     |       |          | MCU |     |
| --- | ---------------- | --------------------------- | --------------------------------------- | --------------------------------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- |
|     |                  | PIR401 1 V 2 C L OL22       | G N D P P I I U U 1 1 2 0 0 1 2     G N | D LDO _3 V 3 P P I I5 U U 1 1 0 0 | 6 5     3 V 3 P I C80 2   PI C8 01   GND |     |     |     |     |     |     |     |     |     |     |     |     |     |       |          |     |     |
|     |                  | PPI C902I C OC LC 929 0 2   | uPHIL）20 P1  I U 1 3 0 3  S W           | V I N 5 P I 4 U 1 0               | 4 PIC1002C    PIC402 C  V B U S          |     |     |     |     |     |     |     |     |     |     |     |     |     |       |          |     |     |
|     |                  | N C                         | （ 2 .2                                  |                                   | COC11 0 0 COC4 4                         |     |     |     |     |     |     |     |     |     |     |     |     |     |       |          |     |     |
|     |                  | PIC901 NC(10uF)             |                                         |                                   | PIC1001 1uFPIC401 10uF                   |     |     |     |     |     |     |     |     |     |     |     |     |     |       |          |     |     |
|     |                  |                             | CH2003V                                 |                                   |                                          |     |     |     |     |     |     |     |     |     |     |     |     |     | COR2  |          |     |     |
|     |                  |                             |                                         |                                   |                                          |     |     |     |     |     |     |     |     |     |     |     |     | 3V3 | R2    | 0Ω VDDIO |     |     |
GND GND 21CP 11CP 01CP 51AP 41AP 31AP 9CP 8CP 7CP 6CP 2FP 1FP 0FP 51DP 41DP 31DP 21DP PIR20C2OR 5  R5 PIR201
|     |     |     |     |     |     |     |     |     |     |     | PIU2051 PIU2050 PIU2049 PIU2048 PIU2047 PIU2046 PIU2045 PIU2044 PIU2043 PIU2042 PIU2041 PIU2040 PIU2039 PIU2038 PIU2037 PIU2036 PIU2035  |                     |                 |         |     |     |     |     | PIR50C2OR 10 PIR501  | 0Ω VDD33        |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------- | ------- | --- | --- | --- | --- | -------------------- | --------------- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |                                                                                                                                          |                     |                 | CUOU22  |     |     |     |     | R100Ω                |                 |     |     |
|     |     |     |     |     |     |     |     |     |     |     | 1 5 0 5 9 4 8 4 7 4 6 4 5 4                                                                                                              | 4 4 3 4 24 14 04 93 | 8 3 7 3 6 3 5 3 |         |     |     |     |     | PIR1002              | PIR1001  VDD33A |     |     |
CH32H417WEU6
|     |     |     |     |     |     |     |     |     |     |     | 2 1 1 1 0 1 5 1 4 1 3 1A 9 C | 8 C 7 C 6CP 2FP 1FP | 0FP 5 1 4 1 3 1 2 1 |     |     |     |     |       |           |          |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | ------------------- | ------------------- | --- | --- | --- | --- | ----- | --------- | -------- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     | C P C P C P A P A P P P      | P P                 | D P D P D P D P     |     |     |     |     |       | COR11     |          |     |     |
| B   |     |     |     |     |     |     |     |     |     |     |                              |                     |                     |     |     |     |     |       | R11NC(0Ω) | VIO_1.8  |     | B   |
|     |     |     |     |     |     |     |     |     |     |     |                              |                     |                     |     |     |     |     | VDDIO | PIR1102   | PIR1101  |     |     |
COC23
|     |     |     | C23 |     |     | XTAL |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PIC2301 PIC2302  PIY201  XI PD0 PD1 PIU2052  5 5 2 3 P D 0 PD11 PIU2034  34 33 PD11 PD10 LED
18pF 1 PD2 P I U 2 5 0 4 5 3   P D 1 PD10 P I U 32 2 0 3 3   PB14 COC4 C43 3   10uF COLED1  LED1
GND COY2  Y2 PD3 P I U 2 5 0 5 5 4   P D 2 PB14 P I U 3 2 1 0 3 2   PB13 P IC 4302 PIC4301  COR16  R16 LED1
COC25  C25 PIY203  25M PD4 PIU2055  5 6 P D 3 @VDD33 power P B 1 3 PIU2031  3 0 PB12 GND VDDIO PIR1601  PIR1602 PILED101 PILED102
3 XO PD5 PIU2056  5 7 P D 4 P B 1 2 PIU2030  2 9 VDDIO COC26  C260.1uF 1k
PIC2501 PIC2502  PIR3002  PD6 PIU2057  5 8 P D 5 @VDDIO power V D D I O PIU2029  2 8 VIO_1.8 PIC2601 PIC260C2O C27  C270.1uF
18pF COR30  R 3 0 PD7 P I U 2 5 0 9 5 8   P P D D 6 7 V P I O B 1 1 8 1 P I U 2 2 7 0 2 8   PB11 PIC2701 PIC2702  GND COR18  COLED2  LED2
PIR3001  10 0 K(NC) PF3 P I U 2 6 0 0 5 9   P F 3 @VIO18 power P B 1 0 P I U 2 2 6 0 2 7   PB10 VDDIO R18 LED2
GND PF4 PIU2060  PIU2061  6 1 P F 4 @VDD12 power PE15 PIU2026  PIU2025  25 PE15 PICCO2C92092  PIC2901  C292.2uF PIR1801  1k PIR1802 PILED201 PILED202
|     |     |     |     |     |     |     |     | PF5 | PIU2062  62 PF5    |     |     |     |     | PE14 PIU2024  24 | PE14 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | ---------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | PE0 | PIU2063  6 3 P E 0 |     |     |     |     | PE13 PIU2023  23 | PE13 |     |     |     |     |     |     |     |
KEY CCOC3300  PE1 PIU2064  6 4 P E 1 PB1/ADC9/OP1_N0/CMP_N0 PIU2022  22 PB1 ETH
|     |     |     | 3V3 |     |     |     |     | PF14 VIO_1. | P 8 I U 2 66 6 0 5 6 5   P F1 4 |     |     |     | PB0/ADC8/OP1_P0/CMP_P0 | P I U 21 20 | 2 0 2 1   PB0 PA5 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------------------- | --- | --- | --- | ---------------------- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
P I R 1 7 0 1   P IC3 002   PI C3 001  PB8 USBHS_DP P I U 2 6 0 7 6 6   VIO18 PA5/ADC5/OP1_O1/DAC2 P I U 1 2 9 0 2 0   VDD33A
COR17  R17 0 .1 u F PB9 USBHS_DM P I U 2 6 0 8 6 7  P B 8 / U S B 2 D P /S W C L K V D D 3 3 A P I U 1 2 8 0 1 9   PC3 PICCO5C15012  PIC5101  C510.1uF GND
|     |                |                    | 10K                   |               |     |     | G N D |     | P I U 2 0 6 8   P B 9 / U S | B 2 D M /S W D I O |        |     | PC3/ADC13/HSADC3 0P_3PO/2CDASH/21CDA/2CP | /O P 3 _ N 0 P I U | 2 0 1 8   |     |     |        |     |       |           |     |
| --- | -------------- | ------------------ | --------------------- | ------------- | --- | --- | ----- | --- | --------------------------- | ------------------ | ------ | --- | ---------------------------------------- | ------------------ | --------- | --- | --- | ------ | --- | ----- | --------- | --- |
|     |                |                    | KEY P I R 1 7 0 2   1 | 2             |     |     |       |     |                             |                    |        |     |                                          |                    |           |     |     |        |     |       |           |     |
|     |                |                    | PIS201CO S2  S2 1     | 2 PIS202  GND |     |     |       |     |                             |                    |        |     |                                          |                    |           |     |     |        |     |       |           |     |
| C   |                |                    | USER                  |               |     |     |       |     |                             |                    |        |     | 0CDASH/01CDA/0CP 1CDASH/11CDA/1CP        |                    |           |     |     |        |     |       |           | C   |
|     | COP6           |                    |                       |               |     |     |       |     |                             |                    |        |     |                                          |                    |           |     |     |        |     | COP7  |           |     |
|     |                | P6                 |                       |               |     | PIN |       |     |                             |                    |        |     |                                          |                    |           |     |     |        |     | P7    | HR911105A |     |
|     | 3V3 3V3PIP601  | 1 2 PIP602 3V3 3V3 |                       |               |     |     |       |     |                             |                    | A21DDV |     |                                          |                    |           |     |     | COC37  |     |       | J 8       |     |
P C 0 PIP603  3 4 PIP604  P C 1 BXTSS AXTSS BXRSS AXRSS 33DDV KDDV NRIDM P R N T P T 3 3 C 3 7 M D I R N PIP706  6 5 R D - J 7
P C 2 PIP605  5 6 PIP606  P C 3 SSV I D I D I D D D O G N D PIC3701 PIC3702  M D I R P PIP705  3 J 6 R X -
P A 5 PIP607  7 8 PIP608  P B 0 M M M V I X X 0 . 1 u F PIP703  R D + J 5
P B 1 PIP609  9 1 0 PIP6010  P E 1 3 COP9  P9 PIU200  PIU201 PIU202 PIU203 PIU204 PIU205 PIU206 PIU207 PIU208 PIU209 PIU2010 PIU2011 PIU2012 PIU2013 PIU2014 PIU2015 PIU2016 PIU2017  COC39  C 3 9 M D I T N 2 T D - J 4
P E 1 PIP6011  4 1 1 1 2 PIP6012  P E 1 5 3V3 3 V 3 0 1 2 3 4 5 6 7 8 9 0 1 1 1 2 1 3 1 4 1 51 61 71 PIP702  4 J 3 R X +
P B 1 PIP6013  0 1 3 1 4 PIP6014  P B 1 1 V D D 3 PIP901  3 A 1 2 PIP902  3 V 3 G N D PIC3901 PIC3902  M D I T P PIP704  1 J 2 T X -
P B 1 PIP6015  2 1 1 5 7 1 1 6 8 PIP6016  P B 1 3 V D D 3 PIP903  3 3 5 4 6 PIP904  3 V 3 NXT_SSBSU PXT_SSBSU A2.1_DDV NXR_SSBSU PXR_SSBSU 33DDV KDDV NRIDM PRIDM NTIDM PTIDM 33DDV 0 . 1 u F PIP701  T D + J 1 T X +
P B 1 PIP6017  4 1 9 2 0 PIP6018  P D 1 0 V D D I PIP905  O 7 8 PIP906  3 V 3 OX 0CP 1CP 2CP 7 N C 10 0 0 pF
P D 1 PIP6019  P I 1 P 6 0 2 1   2 1 2 2 PIP6020  P I P 6 0 2 2   P D 1 2 V GNDP I O _ 1 PIP907  .8 I P 9 0 9   9 1 0 PIP908  P I P 9 0 1 0   3 V 3 GND IX VDDIO PIP707  2 K V 4X 7 5  o h ms
P D 1 P I 3 P 6 0 2 3   2 3 2 4 P I P 6 0 2 4   P D 1 4 PI P 9 0 1 1   1 1 1 2 P I P 9 0 1 2   3 V 3 CDOD1100  PIP708  8 G N D
|     | P D 1 PIP6025  5 | 2 5 2 6 PIP6026  P F 0 |     | GND PIP9013  | 1 3 1 4 PIP9014  G N D |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | ---------------------- | --- | ------------ | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
GND PIP6027  2 7 2 8 PIP6028  G N D V GNDPIP9015  B U S _ USB 1 5 1 6 PIP9016  G G N N D D PID1001 PID1002  E L E D COR21  R PIR2101  1 211 k PIR2102  PIP709  1 9 0
|     |     |     |     | PIP9017  | 1 7 1 8 PIP9018  |     |     |     |     |     |     |     |     |     |     |     |     |     |     | PIP7010  |     |     |
| --- | --- | --- | --- | -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
COP8  P8 COC35 PIC3502  C35 PIC3C602 OC36 PIC4C102 OC41  C36 C41 PIC4C502 OC45 PIC4C601 OC46 COC4PIC24202   C45 C46 C42 PIC4C002 OC40  C40 Diode COR22  R22 1k 12
|     | G N D | K E Y |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | ELED0 PIR2201  | PIR2202  | PIP7012  11 |     |     |
| --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | ----------- | --- | --- |
P F 1 PIP801  1 2 PIP802  P F 2 2.2uF PIC3501  PIC3601  0.1uF PIC4101  0.1uF PIC4501  0.1uF PIC4602  2.2uF PIC4201  0.1uF PIC4001  10uF PIP7011
|     | P C 6 PIP803  | 3 4 PIP804  P C 7 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P C 8 PIP805  5 7 6 8 PIP806  P C 9 P F 0 COR23  R 2 3 E L E D 1
|     | P A 1 PIP807  3 | 9 1 0 PIP808  P A 1 4 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 0Ω PIR2301  PIR2302  |     |     |
| --- | --------------- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- |
P A 1 PIP809  5 1 1 1 2 PIP8010  P C 1 0 GND GND GND GND P F 2 COR24  R 2 4 E L E D 0
P C 1 PIP8011  PIP8013  1 1 3 1 4 PIP8012  PIP8014  P C 1 2 COP3  P3 PIR2401  0Ω PIR2402
D P D 0 PIP8015  1 5 1 6 PIP8016  P D 1 3 V 3 PIP301  1 2 PIP302  GND D
|     | P D 2 PIP8017        | 1 7 1 8 PIP8018  P D 3       |     | G N D PIP303  3       | 4 PIP304  GND     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------- | ---------------------------- | --- | --------------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | P P D D 4 6 PIP8019  | 1 9 2 0 PIP8020  P P D D 5 7 |     | P P B B 8 9 PIP305  5 | 6 PIP306  GND GND |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | P F 3 PIP8021        | 2 1 2 2 PIP8022  P F 4       |     | PIP307  7             | 8 PIP308          |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
P F 5 PIP8023  2 3 2 4 PIP8024  P E 0 If VIO18 is below 1.8V, the Ethernet port indicator circuit needs to be revised.
P E 1 PIP8025  2 5 2 6 PIP8026  P F 1 4 The Ethernet port LED cannot work.
L E D PIP8027  1 2 7 2 8 PIP8028  L E D 2 To prevent current backflow,do not populate resistor R21 and R22.
|     | G N PIP8029  D | 2 9 3 0 PIP8030  G N D     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 3V3 PIP8031    | 3 33 1 34 3 2 PIP8032  3V3 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | PIP8033        | PIP8034                    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     |                | 1                          |     | 2   |     | 3   |     |     | 4   |     |     | 5   |     |     | 6   |     |     | 7   |     |     | 8   |     |

| USBSS |          |     |     |     | DEBUG |     |     |          | MCU |           |             |     |     |     |               |          |          |     |     |
| ----- | -------- | --- | --- | --- | ----- | --- | --- | -------- | --- | --------- | ----------- | --- | --- | --- | ------------- | -------- | -------- | --- | --- |
|       | GND      |     |     |     |       |     |     |          |     |           |             |     |     |     | PIC102        |          |          |     |     |
|       |          |     |     |     |       |     |     |          |     |           |             |     |     |     | COC1  C1      | COC2  C2 | COC3  C3 |     |     |
|       | COP1  P1 |     |     |     |       |     |     | P2 COP2  |     | COR1  R 1 | 0 R V D D K |     |     |     | PIC101  0.1uF |          |          |     |     |
0 +5V TX6 1V2 COR2 PIR102  R 2 PIR101  0 R VD D 1 2A PIC202 PIC201 PIC302 PIC301
|     | G N D 1 |     |     |     |     |     | SWCLK | PIP201  1 |     | PIR202  | PIR201  |     |     |     |     | 0.1uF | 0.1uF |     |     |
| --- | ------- | --- | --- | --- | --- | --- | ----- | --------- | --- | ------- | ------- | --- | --- | --- | --- | ----- | ----- | --- | --- |
V B U S PIP101  2 U S B _ U D _ n PIC401  PIR502  SWDIO PIP202  2 COR3  R 3 0 R V D D 3 3
D n PIP102  3 U S B _ U D _ p COC4  C4 COR5  R 5 PIP203  3 3V3 COR6 PIR302  R 6 PIR301  0 R V D D 3 3A
|     | D p PIP103  |     | PIC402  | 1K  |     |     |     | PIP204  4 |     | COR7 PIR602  | PIR601  |     |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- | --- | --------- | --- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
G N D PIP104  4 GND 47uF PIR501  3V3 PIP205  5 R7 PIR702  PIR701  0R VDDIO
S S R X - PIP105  5 U S B _ S S R X _ p PILED101  +5V PIP206  6 63PFU 53PFU 43PFU 33PFU 23PFU 13PFU 03PFU 33DDV 92PFU 82PFU 72PFU 62PFU 52PFU 81OIV KDDV 42PFU 32PFU 22PFU
|     | S S R X + PIP106  6 U S | B _ S S R X _ n |     | 1   |     |     |     |     |     |     |     |     |     |     | 6XT 11AP 1XR 1XT |     |     |     |     |
| --- | ----------------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
G N D PIP107 COC5  7 COLED1  HE ADER 6 PIU1066 PIU1065 PIU1064 PIU1063  PIU1062 PIU1061 PIU1060  PIU1059 PIU1058 PIU1057  PIU1056 PIU1055 PIU1054  PIU1053 PIU1052 PIU1051  PIU1050 PIU1049 PIU1048 PIU1047 PIU1046 PIU1045
|     | S S T X - 8 C | 5 0 . 1 u F U S B _ S S T X | _ p | PILED102  LED1 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --------------------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S S T X + PIP108 COPCI6C 502 PIC501  9 C 6 0 . 1 u F U S B _ S S T X _ n RED 66 5 4 3 2 1 06 95 85 7 6 5 4 35 2 1 05 94 84 74 6 5
PIP109 PIC602 PIC601  0 2 COU1  U1 6 6 6 6 6 5 5 5 5 5 5 4 4 CH32H417MEU6
G N D PIP100
USB3.0-A COR9  1DP 0 D 2 1 1 1 0 1 5 1 41AP 33DDV 31AP P D M D S U 9CP 8 C 7 C 6CP 81OIV KDDV 2FP 1 F 0 F
|       |     |     |     |     |     |                                      | 1 2  | R9 LED1 |     |     |     |     | P   | C P C P C P A P | _ D _ I _ G   | B P P | P P |     |     |
| ----- | --- | --- | --- | --- | --- | ------------------------------------ | ---- | ------- | --- | --- | --- | --- | --- | --------------- | ------------- | ----- | --- | --- | --- |
|       | GND |     |     |     |     | 3V3 COPLIELDE2D 201 PILED202 PIR902  |      | PIR901  |     |     |     |     |     |                 | G T G T       | V _   |     |     |     |
|       |     |     |     |     |     | LED2                                 | BLUE | 470Ω    |     |     |     |     |     |                 | O / T O O /   | G     |     |     |     |
| POWER |     |     |     |     |     |                                      |      |         |     |     |     |     |     |                 | 2 1 / 1 0 1 A | T O   |     |     |     |
A P 1 A P / 9
|     |     |     |     |     |     |                                |     | COR10  R10    |     |     |     |     |     |     | P   | A P |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | 3V3 PILED301 PILED302 PIR1002  | 1 2 | PIR1001  LED2 |     |     |     |     |     |     |     |     |     |     |     |
COLED3  LED3 GREEN470Ω UFP37 PIU1067  6 7 P D 2 PD15 PIU1044  44 UFP21
|     |     |     |     |     |     |     |     |     |     |     | UFP38 PIU1068  | 6 8 P D 3 |     |     |              |     |     | P D 1 4 PIU1043  4 3 UFP20 |                                      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | --- | ------------ | --- | --- | -------------------------- | ------------------------------------ |
|     |     |     |     |     |     |     |     |     |     |     | UFP39 PIU1069  | 6 9 P D 4 |     |     |              |     |     | P D 1 3 PIU1042  4 2 UFP19 |                                      |
|     |     |     |     |     |     |     |     |     |     |     | UFP40          | 7 0 P D 5 |     |     |              |     |     | P D 1 2 4 1 UFP18          |                                      |
|     |     |     |     |     |     |     |     |     |     |     | UFP41 PIU1070  | 7 1 P D 6 |     |     |              |     |     | P D 1 1 PIU1041  4 0 UFP17 |                                      |
|     |     |     |     |     |     |     |     |     |     |     | UFP42 PIU1071  | 7 2 P D 7 |     |     |              |     |     | P D 1 0 PIU1040  3 9 UFP16 |                                      |
|     | GND |     |     |     |     |     |     |     |     |     | UFP43 PIU1072  | 7 3       |     |     | @VDD33 power |     |     | PIU1039  38 UFP15          |                                      |
|     |     |     |     |     |     |     |     |     |     |     | UFP44 PIU1073  | 74 P F 3  |     |     |              |     |     | PB14 PIU1038  37 UFP14     | PIC1202 COC12  C12 PIC1402 CCOC1144  |
|     |     |     |     |     |     |     |     |     |     |     | UFP45 PIU1074  | 7 5 PF4   |     |     | @VDDIO power |     |     | PB13 PIU1037  36 UFP13     |                                      |
PIR1102  UFP46 PIU1075  7 6 P F5 PB12 PIU1036  35 VDDIO PIC1201  0.1uF PIC1401 10uF
|     |     |     |     |     |     |     |     |     |     |     | UFP47 PIU1076  | 7 7 P E 0 |     |     | @VIO18 power |     |     | VDDIO PIU1035  34 VIO18 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | --- | ------------ | --- | --- | ----------------------- | --- |
C R O R 11 1 1  C C13 O C 1 3   PF14 P I U 1 78 0 7 7   P E 1 VIO18 P I U 33 1 0 3 4 UFP12   P I C 1 5 0 2  COC15  C15 P I C 2 8 0 2  CC OC 2 288
PI R 1 1 0 1   N C (2 0 0 k ) VIO18 P I U 1 79 0 7 8   PF14 PB11 P I U 32 1 0 3 3 UFP11
CU OU2 2   CPO P33  P I C 1 3 0 2   P I C 1 3 0 1   RX8 P I U 1 8 0 0 7 9   VIO18 @VDD12 power PB10 P I U 31 1 0 3 2 UFP10   P I C 1 5 0 1   0.1uF P I C 2 8 0 1   2 . 2 u F
CC OC7 7  P I C 7 0 2   P I R 4 0 2   C O R 4   P I U 1 0 8 0   P B 3 / C C 1 PE15 P I U 1 0 3 1
R 4 3V3 P I P 3 0 1   1 2 P I P 3 0 2 3V3   0.1uF TX8 P I U 1 8 0 1 8 1   P B 4 / C C 2 P E 1 4 P I U 3 0 1 0 3 0 UFP9
)P I C 7 0 1   0 Ω 1 6 CC O C 88  U F P 0 P I P 3 0 3   3 4 P I P 3 0 4 G   N D SWCLK USB_UD_p P I U 1 8 0 2 8 2   P B 8 / U S B 2 D P /S W C L K P E 1 3 P I U 2 9 1 0 2 9 UFP8
NC(4.7 p F P I R 4 0 1   1 V 2 C O L2 2  P I U 2 2 0 1   N C . F B P I5 U 2 0 6   3 V 3 1 0 u F G N D P I P 3 0 5   5 6 P I P 3 0 6 G   N D SWDIO USB_UD_n P I U 1 8 0 3 8 3   P B 9 / U S B 2 D M /S W D I O P E 1 2 P I U 2 8 1 0 2 8 UFP7
L GND P I U 2 3 0 2   G N D LDO _3 V 3 P I 4 U 2 0 5   P I C 8 0 2   PI C8 01   GND U F P 1 7 8 U F P C LK USB_SSTX_n 8 4 S S T X N PE11 27 UFP6
PP I C 9 0 I 2 C   OL C 9 2   0 2   PIL201 P  I U 2 0 3   S W V I N 5P I U 2 0 4 P I C 1 0 0 2 C    OC 11 0 0  P I C 1 1 0 2 C   OC 11 1 + 1  5 V U F P 3 P I P 3 0 7   9 1 0 P I P 3 0 8 U   F P 2 USB_SSTX_p P I U 1 8 0 5 8 4   S S T X P 0N_3PO/3CDASH/31CDA/3CP P E 1 0 P I U 2 6 1 0 2 7 UFP5
C 9 2 . 2 u H C C U F P 6 P I P 3 0 9   1 1 1 2 P I P 3 0 1 0 U   F P 4 P I C 2 0 0 2  COC20  P I C 1 9 0 2   VDD12A P I U 1 8 0 6 8 5   V D D 1 2A 0P_3PO/2CDASH/21CDA/2CP PB1/ADC9/CMP_N0/OP1 _ N 0 P I U 2 5 1 0 2 6 UFP4
P I C 9 0 1   1 0 u F P I C 1 0 0 1   1 u F P I C 1 1 0 1   1 0 u F U F P 7 P I P 3 0 1 1   1 3 1 4 P I P 3 0 1 2 U   F P 5 C20 C C19 O C 1 9   USB_SSRX_n P I U 1 8 0 7 8 6   S S R X N PB 0 /A D C 8 /O P 1 _ P 0 /C M P _ P 0 P I U 2 4 1 0 2 5 UFP3
U F P 9 P I P 3 0 1 3   P I P 3 0 1 4 U   F P 1 0 USB_SSRX_p P I U 1 8 0 8 8 7   P I U 2 3 1 0 2 4 LED2
C H 2 0 03V U F P 1 2 P I P 3 0 1 5   1 5 1 6 P I P 3 0 1 6 U   F P 8 P I C 2 0 0 1   2.2uF P I C 1 9 0 1   0.1uF P I U 1 0 8 8   S S R X P 0 C 1 C P A 5/ A D C 5/ O P 1 _ O 1 /D A C 2 P I U 1 0 2 3
|     |     |     |     |     |     |     | U F P 1 3 P I P 3 | 0 1 7   1 7 1 8 P I P 3 0 1 8 U   F P 1 6 |     |     |     |     | P   | N P N |     | D D | 0O_3PO/0CDA/0AP |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --------------- | --- | --- |
G N D G N D U F P 1 5 P I P 3 0 1 9   1 9 2 0 P I P 3 0 2 0 U   F P 1 1 X T X T X R X R A S A S 1CAD/4CDA/4AP
|           |     |     |     |     |     |     | U F P 1 8 P I P 3 | 0 2 1   2 1 2 2 P I P 3 0 2 2 U   F P 1 9 |     |     |                                        |     | _ S                                  | _ S _ S _ S           |                                                 | H H                                                                       |             |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ----------------- | ----------------------------------------- | --- | --- | -------------------------------------- | --- | ------------------------------------ | --------------------- | ----------------------------------------------- | ------------------------------------------------------------------------- | ----------- | --- | --- |
|           |     |     |     |     |     |     | U F P 1 7 P I P 3 | 0 2 3   2 3 2 4 P I P 3 0 2 4 U   F P 1 4 |     |     |                                        |     | E                                    | E E E                 |                                                 | / 0 1 / 1 1                                                               |             |     |     |
|           |     |     |     |     |     |     | U F P 2 0 P I P 3 | 0 2 5   2 5 2 6 P I P 3 0 2 6 U   F P 2 1 |     |     | C C23 O C 2 3                          |     | D R                                  | D R D R D R           |                                                 | C C                                                                       | A33DDV      |     |     |
|           |     |     |     |     |     |     | U F P 2 2 P I P 3 | 0 2 7   2 7 2 8 P I P 3 0 2 8 U   F P 2 3 |     |     | XI                                     |     | 33DDV E S                            | E S E S E S KDDV N R  | P R N T P T 3 3                                 | TS D A D A                                                                | OIDDV       |     |     |
|           |     |     |     |     |     |     | P I P 3           | 0 2 9   2 9 3 0 P I P 3 0 3 0             |     |     | P I C 2 3 0 1   P I C 2 3 0 2  PIY101  |     | SSV / 3                              | / 4 / 5 / 6 I D       | I D I D I D D D                                 | O / 0 / 1                                                                 |             |     |     |
|           |     |     |     |     |     |     | G N D P I P 3     | 0 3 1   3 1 3 2 P I P 3 0 3 2 G   N D     |     |     | 1                                      |     | E P                                  | E P E P E P M         | M M M V IX                                      | X RN C P C P                                                              |             |     |     |
|           |     |     |     |     |     |     | UFP24 P I P 3     | 0 3 3   3 3 3 4 P I P 3 0 3 4 UFP36       |     |     | 20pF COY1  Y1                          |     | PIU100  PIU101 PIU102 PIU103 PIU104  | PIU105 PIU106 PIU107  | PIU108 PIU109 PIU1010  PIU1011 PIU1012 PIU1013  | PIU1014 PIU1015 PIU1016  PIU1017 PIU1018 PIU1019 PIU1020 PIU1021 PIU1022  |             |     |     |
|           |     |     |     |     |     |     | UFP25 PIP3035 35  | 36PIP3036  UFP37                          |     |     | COC24  PIY103  25M                     | 0   | 1 2 3                                | 4 5 6 7 8             | 9 0 1 21 3                                      | 4 5 6 71 81                                                               | 91 02 12 22 |     |     |
|           |     |     |     |     |     |     | UFP26 PIP3037 37  | 38PIP3038  UFP38                          |     |     | C24 3                                  |     |                                      |                       | 1 1 1                                           | 1 1 1                                                                     |             |     |     |
|           |     |     |     |     |     |     | UFP27 PIP3039 39  | 40PIP3040  UFP39                          |     |     | PIC2401 PIC2402 PIR1502  XO            |     |                                      |                       |                                                 |                                                                           |             |     |     |
|           |     |     |     |     |     |     | UFP28 PIP3041 41  | 42PIP3042  UFP40                          |     |     |                                        |     |                                      |                       |                                                 |                                                                           |             |     |     |
| SPI FLASH |     |     |     |     |     |     | UFP29             | UFP41                                     |     |     | 20pF COR15  R15                        |     |                                      |                       |                                                 |                                                                           | A33DDV      |     |     |
|           |     |     |     |     |     |     | UFP30 PIP3043 43  | 44PIP3044  UFP42                          |     |     | NC                                     |     |                                      | OSIM_IPS ISOM_IPS     |                                                 |                                                                           | OIDDV       |     |     |
|           |     |     |     |     |     |     | UFP31 PIP3045 45  | 46PIP3046  UFP43                          |     |     | PIR1501                                |     | 33DDV SC_IPS KCS_IPS                 | KDDV                  |                                                 | KLCPFU                                                                    |             |     |     |
|           |     |     |     |     |     |     | UFP32 PIP3047 47  | 48PIP3048  UFP44                          |     |     |                                        |     |                                      |                       | 33DDV                                           | TSRN 0PFU 1PFU 2PFU                                                       | 1DEL        |     |     |
|           |     |     |     |     |     |     | UFP33 PIP3049 49  | 50PIP3050  UFP45                          |     |     |                                        |     |                                      |                       | IX OX                                           |                                                                           |             |     |     |
|           |     |     |     |     |     |     | UFP34 PIP3051 51  | 52PIP3052  UFP46                          |     |     |                                        |     |                                      |                       |                                                 |                                                                           |             |     |     |
|           |     |     |     |     |     |     | UFP35 PIP3053 53  | 54PIP3054  UFP47                          |     |     |                                        |     |                                      |                       |                                                 |                                                                           |             |     |     |
COU4  U4 3V3 GND PIP3055 55 56PIP3056  GND COS1  S1 PIC3202 COC32  C32 PIC3302 COC33  C33 PIC3402 COC34  C34 PIC2502 COC25  C25 PIC2602 COC26  C26 PIC3502 COC35  C35 PIC2702 COC27  C27
|     |     |     |     | COC29  |     |     | PIP3057 57 | 58PIP3058  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S P I _ C S PIU401  1 C S V C C PIU408  8 C 2 PIC2902 PIC2901  9 0.1uF RX8 TX1 PIP3059 59 60PIP3060  RX1 TX8 NRST PIS101  1 1 2 PIS102  2 GND PIC3201  PIC3301  PIC3401  PIC2501  PIC2601  PIC3501  PIC2701
S P I _ M ISO PIU402  2 D 0 HO L D PIU407  7 COC30  0.1uF 0.1uF2.2uF 0.1uF 10uF 0.1uF 0.1uF
3 V 3 PIU403  3 W P CL K PIU406  6 SP I _ S C K HEADER 30x2 C30 PIC3002 PIC3001  0.1uF
|     |         | 4 G N D D I | 5 S     | P I _ M O SI |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | ----------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | PIU404  |             | PIU405  |              |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
SPI FLASH
NC

| USBSS |          |     |     |     | DEBUG |     |     |          | MCU |           |             |     |     |     |         |          |                   |     |     |
| ----- | -------- | --- | --- | --- | ----- | --- | --- | -------- | --- | --------- | ----------- | --- | --- | --- | ------- | -------- | ----------------- | --- | --- |
|       | GND      |     |     |     |       |     |     |          |     |           |             |     |     |     | PIC102  |          |                   |     |     |
|       |          |     |     |     |       |     |     |          |     |           |             |     |     |     |         | COC1  C1 | COC2  C2 COC3  C3 |     |     |
|       | COP1  P1 |     |     |     |       |     |     | P2 COP2  |     | COR1  R 1 | 0 R V D D K |     |     |     | PIC101  | 0.1uF    |                   |     |     |
0 +5V TX6 1V2 COR2 PIR102  R 2 PIR101  0 R VD D 1 2A PIC202 PIC201 PIC302 PIC301
|     | G N D 1 |     |     |     |     |     | SWCLK | PIP201  1 |     | PIR202  | PIR201  |     |     |     |     |     | 0.1uF 0.1uF |     |     |
| --- | ------- | --- | --- | --- | --- | --- | ----- | --------- | --- | ------- | ------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
V B U S PIP101  2 U S B _ U D _ n PIC401  PIR502  SWDIO PIP202  2 COR3  R 3 0 R V D D 3 3
D n PIP102  3 U S B _ U D _ p COC4  C4 COR5  R 5 PIP203  3 3V3 COR6 PIR302  R 6 PIR301  0 R V D D 3 3A
|     | D p PIP103  |     | PIC402  | 1K  |     |     |     | PIP204  4 |     | COR7 PIR602  | PIR601  |     |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- | --- | --------- | --- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
G N D PIP104  4 GND 47uF PIR501  3V3 PIP205  5 R7 PIR702  PIR701  0R VDDIO
S S R X - PIP105  5 U S B _ S S R X _ p PILED101  +5V PIP206  6 63PFU 53PFU 43PFU 33PFU 23PFU 13PFU 03PFU 33DDV 92PFU 82PFU 72PFU 62PFU 52PFU 81OIV KDDV 42PFU 32PFU 22PFU
|     | S S R X + PIP106  6 U | S B _ S S R X _ n |     | 1   |     |     |     |     |     |     |     |     |     |     |     | 6XT 11AP 1XR 1XT |     |     |     |
| --- | --------------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
G N D PIP107 COC5  7 COLED1  HE ADER 6 PIU1066 PIU1065 PIU1064 PIU1063  PIU1062 PIU1061 PIU1060  PIU1059 PIU1058 PIU1057  PIU1056 PIU1055 PIU1054  PIU1053 PIU1052 PIU1051  PIU1050 PIU1049 PIU1048 PIU1047 PIU1046 PIU1045
|     | S S T X - 8 | C 5 0 . 1 u F U | S B _ S S T X _ p | PILED102  LED1 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------- | --------------- | ----------------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S S T X + PIP108 COPCI6C 502 PIC501  9 C 6 0 . 1 u F U S B _ S S T X _ n RED 66 5 4 3 2 1 06 95 85 7 6 5 4 35 2 1 05 94 84 74 6 5
PIP109 PIC602 PIC601  0 2 COU1  U1 6 6 6 6 6 5 5 5 5 5 5 4 4 CH32H417MEU6
G N D PIP100
USB3.0-A COR9  1DP 0 D 2 1 1 1 0 1 5 1 41AP 33DDV 31AP P D M D S U 9CP 8 C 7 C 6CP 81OIV KDDV 2FP 1 F 0 F
|       |     |     |     |     |     |                                      | 1 2  | R9 LED1 |     |     |     |     |     | P C P | C P C P A P | _ D _ I _ G B P   | P P P |     |     |
| ----- | --- | --- | --- | --- | --- | ------------------------------------ | ---- | ------- | --- | --- | --- | --- | --- | ----- | ----------- | ----------------- | ----- | --- | --- |
|       | GND |     |     |     |     | 3V3 COPLIELDE2D 201 PILED202 PIR902  |      | PIR901  |     |     |     |     |     |       |             | G T G T V _       |       |     |     |
|       |     |     |     |     |     | LED2                                 | BLUE | 470Ω    |     |     |     |     |     |       |             | O / T O O / G     |       |     |     |
| POWER |     |     |     |     |     |                                      |      |         |     |     |     |     |     |       |             | 2 1 / 1 0 1 A T O |       |     |     |
A P 1 A P / 9
|     |     |     |     |     |     |                                |     | COR10  R10    |     |     |     |     |     |     |     | P A P |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     |     |     | 3V3 PILED301 PILED302 PIR1002  | 1 2 | PIR1001  LED2 |     |     |     |     |     |     |     |       |     |     |     |
COLED3  LED3 GREEN470Ω UFP37 PIU1067  6 7 P D 2 PD15 PIU1044  44 UFP21
|     |     |     |     |     |     |     |     |     |     |     | UFP38 | PIU1068  6 8 | P D 3 |     |     |              |     | P D 1 4 PIU1043  4 3 UFP20 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ----- | --- | --- | ------------ | --- | -------------------------- | --- |
|     |     |     |     |     |     |     |     |     |     |     | UFP39 | PIU1069  6 9 | P D 4 |     |     |              |     | P D 1 3 PIU1042  4 2 UFP19 |     |
|     |     |     |     |     |     |     |     |     |     |     | UFP40 | 7 0          | P D 5 |     |     |              |     | P D 1 2 4 1 UFP18          |     |
|     |     |     |     |     |     |     |     |     |     |     | UFP41 | PIU1070  7 1 | P D 6 |     |     |              |     | P D 1 1 PIU1041  4 0 UFP17 |     |
|     |     |     |     |     |     |     |     |     |     |     | UFP42 | PIU1071  7 2 | P D 7 |     |     |              |     | P D 1 0 PIU1040  3 9 UFP16 |     |
|     |     |     |     |     |     |     |     |     |     |     | UFP43 | PIU1072  7 3 |       |     |     | @VDD33 power |     | PIU1039  38 UFP15          |     |
GND UFP44 PIU1073  74 P F 3 PB14 PIU1038  37 UFP14 PIC1202 COC12  C12 PIC1402 CCOC1144
|     |     |     |     |     |     |     |     |     |     |     | UFP45 | PIU1074  7 5 | PF4  |     |     | @VDDIO power |     | PB13 PIU1037  36 UFP13 |                             |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ---- | --- | --- | ------------ | --- | ---------------------- | --------------------------- |
|     |     |     |     |     |     |     |     |     |     |     | UFP46 | PIU1075  7 6 | P F5 |     |     |              |     | PB12 PIU1036  35 VDDIO | PIC1201  0.1uF PIC1401 10uF |
PIR1102  UFP47 PIU1076  7 7 P E 0 @VIO18 power VDDIO PIU1035  34 VIO18
|     |     |     |     |     |     |     |     |     |     |     | COC13  C13 PF14 | P I U 1 78 0 7 7   | P E 1 |     |     |     |     | VIO18 P I U 33 1 0 3 4 UFP12   | PIC1502 COC15  C15 PIC2802 CCOC2288  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------------ | ----- | --- | --- | --- | --- | ------------------------------ | ------------------------------------ |
CROR1111  VIO18 P I U 1 79 0 7 8   PF14 PB11 P I U 32 1 0 3 3 UFP11
PIR1101  NC(200k) CPOP33  PIC1302 PIC1301  RX8 P I U 1 8 0 0 7 9   VIO18 @VDD12 power PB10 P I U 31 1 0 3 2 UFP10   PIC1501  0.1uF PIC2801 2.2uF
|     |     |     | CUOU22  |     |     |     |     |     |     |     |     | P I U 1 0 8 0   | P B 3 / C C 1 |     |     |     |     | PE15 P I U 1 0 3 1   |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | --- | --- | --- | --- | -------------------- | --- |
P I C 7 0 2   P I R 4 0 2   C O R 4   3V3 P I P 3 0 1  1 2 P I P 3 0 2 3V3   0.1uF TX8 P I U 1 8 0 1 8 1   P B 4 / C C 2 P E 1 4 P I U 3 0 1 0 3 0 UFP9
CC OC7 7  R 4 U F P 0 P I P 3 0 3   3 4 P I P 3 0 4 G   N D SWCLK USB_UD_p P I U 1 8 0 2 8 2   P B 8 / U S B 2 D P /S W C L K P E 1 3 P I U 2 9 1 0 2 9 UFP8
)P I C 7 0 1   0 Ω 1 6 CC O C 88  G N D P I P 3 0 5   5 6 P I P 3 0 6 G   N D SWDIO USB_UD_n P I U 1 8 0 3 8 3   P B 9 / U S B 2 D M /S W D I O P E 1 2 P I U 2 8 1 0 2 8 UFP7
NC(4.7 p F P I R 4 0 1   1 V 2 P I U 2 2 0 1   N C . F B P I 5 U 2 0 6   3 V 3 1 0 u F U F P 1 7 8 U F P C LK USB_SSTX_n 8 4 S S T X N PE11 27 UFP6
CL O L2 2  GND P I U 2 3 0 2   G N D LDO _3 V 3 P I 4 U 2 0 5   P I C 8 0 2   PI C8 01   GND U F P 3 P I P 3 0 7   9 1 0 P I P 3 0 8 U   F P 2 USB_SSTX_p P I U 1 8 0 5 8 4   S S T X P 0N_3PO/3CDASH/31CDA/3CP P E 1 0 P I U 2 6 1 0 2 7 UFP5
PP I C 9 0 I 2 C   OL C 9 2 9  0 2   PIL201 P  I U 2 0 3   S W V I N 5 P I U 2 0 4 P I C 1 0 0 2 C     OC 11 0 0  P I C 1 1 0 2 C   OC 11 1 + 1  5 V U F P 6 P I P 3 0 9   1 1 1 2 P I P 3 0 1 0 U   F P 4 P I C 2 0 0 2  COC20  P I C 1 9 0 2   VDD12A P I U 1 8 0 6 8 5   V D D 1 2A 0P_3PO/2CDASH/21CDA/2CP PB1/ADC9/CMP_N0/OP1 _ N 0 P I U 2 5 1 0 2 6 UFP4
C 2 . 2uH C C U F P 7 P I P 3 0 1 1   1 3 1 4 P I P 3 0 1 2 U   F P 5 C20 C C19 O C 1 9   USB_SSRX_n P I U 1 8 0 7 8 6   S S R X N PB 0 /A D C 8 /O P 1 _ P 0 /C M P _ P 0 P I U 2 4 1 0 2 5 UFP3
P I C 9 0 1   1 0 u F P I C 1 0 0 1   1 u F P I C 1 1 0 1   1 0 u F U F P 9 P I P 3 0 1 3   P I P 3 0 1 4 U   F P 1 0 USB_SSRX_p P I U 1 8 0 8 8 7   P I U 2 3 1 0 2 4 LED2
U F P 1 2 P I P 3 0 1 5   1 5 1 6 P I P 3 0 1 6 U   F P 8 P I C 2 0 0 1   2.2uF P I C 1 9 0 1   0.1uF P I U 1 0 8 8   S S R X P 0 C 1 C P A 5/ A D C 5/ O P 1 _ O 1 /D A C 2 P I U 1 0 2 3
C H 2 0 03V U F P 1 3 P I P 3 0 1 7   1 7 1 8 P I P 3 0 1 8 U   F P 1 6 P N P N D D 0O_3PO/0CDA/0AP
|     |     |     |     |     |     |     | U F P 1 5 P I P 3 | 0 1 9   1 9 2 0 P I P 3 0 2 0 U   F P 1 1 |     |     |     |     |     | X T X T | X R X R | A S | A S 1CAD/4CDA/4AP |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------------------------------------- | --- | --- | --- | --- | --- | ------- | ------- | --- | ----------------- | --- | --- |
G N D G N D U F P 1 8 P I P 3 0 2 1   2 1 2 2 P I P 3 0 2 2 U   F P 1 9 _ S _ S _ S _ S H H
|           |     |          |     |     |     |     | U F P 1 7 P I P 3 | 0 2 3   2 3 2 4 P I P 3 0 2 4 U   F P 1 4 |     |     |                                  |     |         | E E                          | E E                                          | / 0 1                                             | / 1 1                                            |     |     |
| --------- | --- | -------- | --- | --- | --- | --- | ----------------- | ----------------------------------------- | --- | --- | -------------------------------- | --- | ------- | ---------------------------- | -------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ | --- | --- |
|           |     |          |     |     |     |     | U F P 2 0 P I P 3 | 0 2 5   2 5 2 6 P I P 3 0 2 6 U   F P 2 1 |     |     | C C23 O C 2 3                    |     |         | D R D R                      | D R D R                                      | C                                                 | C A33DDV                                         |     |     |
|           |     |          |     |     |     |     | U F P 2 2 P I P 3 | 0 2 7   2 7 2 8 P I P 3 0 2 8 U   F P 2 3 |     |     | XI                               |     |         | 33DDV E S E S                | E S E S KDDV N R P R                         | N T P T 3 3 TS D A                                | D A OIDDV                                        |     |     |
|           |     |          |     |     |     |     | P I P 3           | 0 2 9   2 9 3 0 P I P 3 0 3 0             |     |     | P I C 23 0 1   P I C2302 PIY101  |     | SSV     | / 3 / 4                      | / 5 / 6 I D I D                              | I D I D D D O / 0                                 | / 1                                              |     |     |
|           |     |          |     |     |     |     | G N D P I P 3     | 0 3 1   3 1 3 2 P I P 3 0 3 2 G   N D     |     |     | 1                                |     |         | E P E P                      | E P E P M M                                  | M M V IX X RN C P                                 | C P                                              |     |     |
|           |     |          |     |     |     |     | UFP24 P I P 3     | 0 3 3   3 3 3 4 P I P 3 0 3 4 UFP36       |     |     | 20pF COY1  Y1                    |     | PIU100  | PIU101 PIU102 PIU103 PIU104  | PIU105 PIU106 PIU107  PIU108 PIU109 PIU1010  | PIU1011 PIU1012 PIU1013  PIU1014 PIU1015 PIU1016  | PIU1017 PIU1018 PIU1019 PIU1020 PIU1021 PIU1022  |     |     |
|           |     |          |     |     |     |     | UFP25 PIP3035 35  | 36PIP3036  UFP37                          |     |     | COC24  PIY103  25M               |     | 0       | 1 2 3                        | 4 5 6 7 8                                    | 9 0 1 21 3 4 5 6                                  | 71 81 91 02 12 22                                |     |     |
|           |     |          |     |     |     |     | UFP26 PIP3037 37  | 38PIP3038  UFP38                          |     |     | C24 3                            |     |         |                              |                                              | 1 1 1 1 1 1                                       |                                                  |     |     |
|           |     |          |     |     |     |     | UFP27 PIP3039 39  | 40PIP3040  UFP39                          |     |     | PIC2401 PIC2402 PIR1502  XO      |     |         |                              |                                              |                                                   |                                                  |     |     |
|           |     |          |     |     |     |     | UFP28 PIP3041 41  | 42PIP3042  UFP40                          |     |     |                                  |     |         |                              |                                              |                                                   |                                                  |     |     |
| SPI FLASH |     |          |     |     |     |     | UFP29             | UFP41                                     |     |     | 20pF COR15  R15                  |     |         |                              |                                              |                                                   |                                                  |     |     |
|           |     |          |     |     |     |     | UFP30 PIP3043 43  | 44PIP3044  UFP42                          |     |     | NC                               |     |         |                              | OSIM_IPS ISOM_IPS                            |                                                   | A33DDV                                           |     |     |
|           |     |          |     |     |     |     | UFP31 PIP3045 45  | 46PIP3046  UFP43                          |     |     | PIR1501                          |     |         | 33DDV SC_IPS KCS_IPS         | KDDV                                         | 33DDV KLCPFU                                      | OIDDV                                            |     |     |
|           |     |          |     |     |     |     | UFP32 PIP3047 47  | 48PIP3048  UFP44                          |     |     |                                  |     |         |                              |                                              | TSRN 0PFU                                         | 1PFU 2PFU 1DEL                                   |     |     |
|           |     |          |     |     |     |     | UFP33 PIP3049 49  | 50PIP3050  UFP45                          |     |     |                                  |     |         |                              |                                              | IX OX                                             |                                                  |     |     |
|           |     |          |     |     |     |     | UFP34 PIP3051 51  | 52PIP3052  UFP46                          |     |     |                                  |     |         |                              |                                              |                                                   |                                                  |     |     |
|           |     |          |     |     |     |     | UFP35 PIP3053 53  | 54PIP3054  UFP47                          |     |     |                                  |     |         |                              |                                              |                                                   |                                                  |     |     |
|           |     | COU4  U4 | 3V3 |     |     |     | GND PIP3055 55    | 56PIP3056  GND                            |     |     | COS1  S1                         |     |         |                              |                                              |                                                   |                                                  |     |     |
COC2 9   P I P 3 0 5 7   5 7 5 8P I P 3 0 5 8   PIC3202 COC32  PIC3302 COC33  PIC3402 COC34  PIC2502 COC25  PIC2602 COC26  PIC35C02 OC35  PIC2702C OC27
S P I _ C S PIU401  1 C S V C C PIU408  8 C 2 P I 9 C2902 PIC2901  0.1uF RX8 TX1 P I P 3 0 5 9   5 9 6 0 P I P 3 0 6 0 RX1   TX8 NRST PIS101  1 1 2 PIS102  2 GND C32 C33 C34 C25 C26 C35 C27
S P I _ M ISO PIU402  2 D 0 HO L D PIU407  7 COC30  PIC3201  PIC3301  PIC3401  PIC2501  PIC2601  PIC3501  PIC2701
3 V 3 PIU403  3 W P CL K PIU406  6 SP I _ S C K HEADER 30x2 C30 PIC3002 PIC3001  0.1uF 0.1uF 0.1uF 2.2uF 0.1uF 10uF 0.1uF 0.1uF
|     |     | 4 G     | N D D I 5 S | P I _ M O SI |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | PIU404  | PIU405      |              |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
SPI FLASH
NC

|     | 1   |     |     |     | 2   |     |     |     | 3   |     | 4   |     |     | 5   |     |     | 6   | 7   |     | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
POWER&USBPD
POWER&USB
|     | VBUS_CC | COP10  P10        |                   | VBUS |     |     |     |     |     |     |     |     |     |     |     | COP2  | GND     |     |     |     |
| --- | ------- | ----------------- | ----------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --- | --- | --- |
|     |         | PIP1001  1        | 2 PIP1002         |      |     |     |     |     |     |     |     |     |     |     |     | P2    | VBUS_HS |     |     |     |
|     |         | P I P 1 0 0 3   3 | 4 P I P 1 0 0 4   |      |     |     |     |     |     |     |     |     |     |     |     |       | G N D 0 |     |     |     |
P I P 1 0 0 5   5 6 P I P 1 0 0 6   COL1  GND CR O R2255  V B U S P I P 1 2 0 1   COP4  0
VBUS_CC L1 VBUS 1V2 PIR250 2   PINR25C01 (0Ω) VDD_1.2A D n P I P 2 2 0 2 USBHS_DM   P4
A GND HE ADE R 3x2 GND PIC102  PIC202  COC7  PIL101  PIL10P2IC401 C   PIR302  5V PIR2802  CR O R2266  PINR26C01 (0Ω) VDDK D p P I P 3 4 2 0 3 USBHS_DP   DNG 4 A
COC1  C 1 COC2  C 2 C7 NC(4 .7 u H /5 A )C4 OC4  COR3  R3 1V2 PIR260 2   G N D P I P 5 2 0 4   USBSS_RXP GND GND PIP404  3 OTG_FS_DP
NC(22uF/35 PIC101  V ) PIC201  N C(0.1uF) 0 PIU1010 PIU109 PIU108 PIU107 PPIU1I06 C701   PIC702  NC(100nF) PIC402  P I C 3 2 0 2  COC32  P I C 3 3 0 2  COC33  R COR2 288  S S R X - P I P 6 2 0 5   USBSS_RXN U D + P I 2 P 4 0 3   OTG_FS_DM
1 9 8 7 6 CO U1 U1  N C ( 6F8 pB F) NC(15K P I R 3 0 1   ) C32 C33 PIR2801  N C (200k) S S R X + P I P 7 2 0 6   DNG U D - P I 1 P 4 0 2
|     |     |     |     |     |     |     |     |     | P I R 4 0 2   P I C 3 2 0 1   P I C 3 3 0 1   NC(22uF) |     |     | CUOU33  |     |     |     |     | G N D P I P 8 2 0CO C11 7C1  1  0.1uFUSBSS_TXP | +5V P I P | 4 0 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | ------- | --- | --- | --- | --- | ---------------------------------------------- | --------- | ------- | --- |
GND N I N I W S W S T S COR4  RN4C(22uF) CC OC 556 6  P I C 5 6 0 2   P I R 2 7 0 2   R C O R 2 2 7 7  S S S S T T X X + - P I P 9 2 0 COP C12 8 CI 1C  21  1 0 1   P I 0.1uFUSBSS_TXN C 1 1 0 2   PIP400  VBUS_FS
COP1  P1 B12B9 A1A4 G N D A 1 VBUS_CC V V B PIR401  NC(4.7K) P I C 5 6 0 1   N C ( 0 Ω ) 1 6 C CO C88  G N D P I P 0 2 0 P 9 I C   1 2 0 1   P I C 1 2 0 2
V B U S P P I I P P A 1 1 4 0 0 A A 1 4     NC(4.7 p F ) P I R 2 7 0 1   1V 2 CL O L22  P I U 3 2 0 1   N C. F B P I5 U 3 0 6   3 V 3 1 0 u F P I P 2 0 0   0
R F U 1 P I P B 1 8 0 B 8   CO R1 R1  D G N D P I U 3 3 0 2   G N D LDO _3 V 3 P I 4 U 3 0 5   P I C 80 2   PI C8 01   GND USB3.0-A
COR13  R13 C C P I P A 1 5 0 A 5 C   C 1 PIR102 _ 1   PIR101  0Ω CC1 D N I . . N PPIC5702   I CC O L C5 52 7 7 0 2 N   C(2 .2 uH P ) IL20 P1  I U 3 0 3  S W V I N 5 P I U 3 0 4 PIC5302 C   COC55 3 3 PIC5402  CCOC 55 45 4  V GND
| CC2 | PIR130 1   PIR1302         |        | D - P I P B 1 7 0 B 7 O   T G           | _ FS_DM                 |     | N G V A C N                                | C N B F G A |     | GNDGNDGND |     | PIC5701 NC(10uF) |         |     | PIC5301 1uFPIC5401 10uF |     |     |     |     |     |     |
| --- | -------------------------- | ------ | --------------------------------------- | ----------------------- | --- | ------------------------------------------ | ----------- | --- | --------- | --- | ---------------- | ------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
|     | N C (5.1K)                 |        | D + P I P A A 1 6 7 0 A 6 O O   T T G G | _ _ F F S S _ _ D D M P |     | PIU100 PIU101 PIU102 PIU103 PIU104 PIU105  | NC(CH2024Q) |     |           |     |                  |         |     |                         |     |     |     |     |     |     |
| CC1 | C R1 O R12  2              |        | D - P I P B 1 6 0 A 7 O   T G           | _ F S _ D P             |     | 0 1 2                                      | 3 4 5       |     |           |     |                  | CH2003V |     |                         |     |     |     |     |     |     |
|     | PIR1201  NC(5.1K) PIR1202  |        | D + PIP10B6  A 8                        |                         |     |                                            |             |     |           |     |                  |         |     |                         |     |     |     |     |     |     |
|     |                            | R      | F U 1 P I P B 1 5 0 A 8 CC1_2           | CO R9 R9  0Ω CC2        |     | VBUS_CC                                    | BF          |     |           |     | GND              |         |     | GND                     |     |     |     |     |     |     |
|     |                            | A9A12  | C C P I P B 1 4 0 B 5                   | PIR902   PIR901         |     |                                            |             |     |           |     |                  |         |     |                         |     |     |     |     |     |     |
|     |                            | B4B1 V | B U S PIP10B4  B 1                      |                         |     |                                            |             |     |           |     |                  |         |     |                         |     |     |     |     |     |     |
|     |                            | G      | N D PIP10B1  VBUS_CC                    |                         |     |                                            |             |     |           |     |                  |         |     |                         |     |     |     |     |     |     |
TYPE-C
|     |         |                                                |       |         |      |                                       |          |     |     |     |     |     |     |                     | GND                           |     |     |     |     | MCU |
| --- | ------- | ---------------------------------------------- | ----- | ------- | ---- | ------------------------------------- | -------- | --- | --- | --- | --- | --- | --- | ------------------- | ----------------------------- | --- | --- | --- | --- | --- |
|     |         |                                                |       |         |      | P I RC4 O6 R0 426   N P I R 4 6 0 1   |          |     |     |     |     |     |     |                     | P I C 2C C26 6 0 2 O  C 2 6   |     |     |     |     |     |
|     | VBUS_HS | P I RCR 4O5R 0 44 2 5   5 N P C IR 4 ( 5 0 0 1 | Ω   ) | VBUS_FS | C UO | U6 6  R 4 6 C ( 0 Ω                   | )        |     |     |     |     |     |     | PD_SF_GTO MD_SF_GTO |                               |     |     |     |     |     |
|     |         | CU O U 5   5                                   | V B U | S       |      |                                       | U2 V B U | S   |     |     |     |     |     |                     | P I C 2 0.1uF 6 0 1           |     |     |     |     |     |
B V O - P I U 52 0 2   P I C 3 8 0 1   3 V O - P I 6 0 2   P I C 5 8 0 1   B
|     | PIU | 3 503   V I + |                                             |     | PIU | 6 0 3   V I + | 16                                         |     |     |     |     |     |                                                                                                           |                       | 33DDV                    |     |     |     |     |     |
| --- | --- | ------------- | ------------------------------------------- | --- | --- | ------------- | ------------------------------------------ | --- | --- | --- | --- | --- | --------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------ | --- | --- | --- | --- | --- |
|     |     | G N           | D P I U 5 10 1   P I C 3 8 0 2  C OC 33 88  |     |     | G N D         | P I U 0 1   P I C 5 8 0 2   CC O C 55 8 8  |     |     |     |     |     | 11CP 01CP 51AP                                                                                            | 41AP 31AP 9CP 8CP     | 7CP 6CP 01DP 9DP 51EP    |     |     |     |     |     |
|     |     |               | C                                           |     |     | C H 2 1 3     | 1 0 u F                                    |     |     |     |     |     |                                                                                                           | 21AP 11AP             |                          |     |     |     |     |     |
|     |     | C H 2 1 3     | 1 0 u                                       | F   |     |               |                                            |     |     |     |     |     | PIU2045 PIU2044 PIU2043 PIU2042 PIU2041 PIU2040 PIU2039 PIU2038 PIU2037 PIU2036 PIU2035 PIU2034 PIU2033 P |                       | I U 2 0 3 2   P IU2 031  |     |     |     |     |     |
|     |     |               | GND                                         |     |     |               | GND                                        |     |     |     |     |     | 54 4 4 3 4                                                                                                | 24 14 0 4 9 3 8 3 7 3 | 6 3 53 43 33 23 13       |     |     |     |     |     |
COU2  U2
|     |     |     |                  |                  |     |     |     |      |     |     |                       |                    | 3OSIM/3DDS/11CP 3 K 3 | _T1NAC/3LCS/4DDS/41AP _R1NAC/3ADS/31AP T R 1 D 0 D | 7 D 6DDS/6CP ADS_C3I/01DP LCS_C3I/9DP 33DDV 3OISQ/51EP |                          | CH32H416RDU6                 |     |     |     |
| --- | --- | --- | ---------------- | ---------------- | --- | --- | --- | ---- | --- | --- | --------------------- | ------------------ | --------------------- | -------------------------------------------------- | ------------------------------------------------------ | ------------------------ | ---------------------------- | --- | --- | --- |
|     |     |     | COC23  C23       |                  |     |     |     |      |     |     |                       |                    | C SC                  | 1 N 1 N D D                                        | D                                                      |                          |                              |     |     |     |
|     |     |     |                  | XI               |     |     |     | XTAL |     |     |                       |                    | S / 2 S / 1           | A C A C S / 9 S / 8                                | S / 7                                                  |                          |                              |     |     |     |
|     |     |     | PIC2301 PIC2302  | PIY201           |     |     |     |      |     |     |                       |                    | D D S C               | / P D / M C P C P                                  | C P                                                    |                          |                              |     |     |     |
|     |     |     | 18pF             | 1                |     |     |     |      |     |     |                       |                    | S / S / 5             | 1 B D 1                                            |                                                        |                          |                              |     |     |     |
|     |     |     | GND              | PIY203  COY2  Y2 |     |     |     |      |     |     |                       |                    | 0 1 C D D             | S U B S                                            |                                                        |                          |                              |     |     |     |
|     |     |     | COC25  C25       | 25M              |     |     |     |      |     |     | PC12                  | 46 PC12/SDCK/MOSI3 | P S /51AP             | /2 U /1                                            |                                                        | PE9/OP2P0                | 30 PE9                       |     |     |     |
|     |     |     |                  | 3 PIR3002  XO    |     |     |     |      |     |     | PD2 PIU2046           | 47 PD2/SDCMD       |                       | 1 A 1                                              | P                                                      | F 13 / S D A 4 / P I O C | 1 PIU2030  2 9 PF13          |     |     |     |
|     |     |     | PIC2501 PIC2502  | COR30            |     |     |     |      |     |     | PD3 PIU2047  PIU2048  | 4 8 P D 3 / SD     | S TR                  | P A P                                              | PF12/OP                                                | 2 N 1 / S C L4 / P I O C | 0 PIU2029  PIU2028  2 8 PF12 |     |     |     |
|     |     |     | 18pF             | R30              |     |     |     |      |     |     | PB3 CC1 PIU2049       | 4 9 P B 3 / C C    | 1 R / SC K 1          |                                                    | PB1/AD C 9 / O P 1 N                                   | 0 / O P 2 O 1 / C M P N  | 0 PIU2027  2 7 PB1           |     |     |     |
PIR3001  100K(NC) PB4 CC2 P I U 2 5 0 0 5 0   P B 4 / C C 2 R / M I SO 1 P B 0 /A D C 8 / O P 1 P 0 / C M P P 0 P I U 2 2 6 0 2 6   PB0 3V3
GND PB5 P I U 2 51 0 5 1   PB5/MOSI1/CAN2R P C 5 / A D C 1 5 P I U 2 2 5 0 2 5   PC5 COR5  R5
|     |     |     |     |     |     |     |     |     |     |     | PB6 PB7 P I | U 2 5 5 0 2 3 5 2   P B 6 / S CL | 1 /CAN2T |     | PC 4 / A D C 1 | 4 / O P 1 O 0 / C M P N | 1 P I U 2 2 2 3 4 0 2 4   PC4 PA7 | PIR50C2O R7  PIR501  0Ω | VDD33 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------------------------- | -------- | --- | -------------- | ----------------------- | --------------------------------- | ----------------------- | ----- | --- |
3V3 PB8 USBHS_DP P I U 2 5 0 4 5 3   P B 7 / S D A 1 R3NAC/KCSQ/_LCS_C3I/_1SCS/6FP T3NAC/ P A 7 / A D C 7 / O P 1 N 1 P I U 2 2 2 0 2 3   PA6 R7 0Ω
KEY PB9 USBHS_DM PIU2054  5 5 P B 8 / U S B 2 D P /S W C L K P A 6 / A D C 6 / O P 1 P 1 PIU2022  2 1 PA5 PIR702  PIR701  VREF
PIR1701  USBSS_TXN PIU2055  5 6 P B 9 / U S B 2 D M /S W D I O P A 5 / A D C 5 / O P 1 O 1 / D A C 2 PIU2021  2 0 PA4 COR10  R100Ω
COR17  R17 USBSS_TXP PIU2056  5 7 S S T X B S 4 C 5 C 0 0 N P A 4 / A D C 4 / O P 3 O 1 / D A C 1 PIU2020  1 9 PA3 PIR1002  PIR1001  VDD33A
|     |     |     | PIR1702  10K | USER |     |     |     |     |     |     | VDD_1.2A PIU2057  | 5 8 S V S D T D X 1 A 2A |     | C S D A D A | P 3 P 3 P P P | A A 3 2 / / A A D D C C 3 2 / / O O P P 3 3 N P | 1 1 PIU2019  1 8 PA2 |     |     |     |
| --- | --- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | ----------------- | ------------------------ | --- | ----------- | ------------- | ----------------------------------------------- | -------------------- | --- | --- | --- |
C KEY 1 1 2 2 GND COC35 PIC3502  PIC3602 COC36  U S B S S _ R PIU2058  X N 5 9 S S R X B Q /_ S S O / O / PA1/ADC1 PIU2018  17 PA1 C
|     |     |     | PIS201CO S2  | S2 PIS202  |     |     |     |     |     | C35 | C36 U S B S S _ R PIU2059  X P | 6 0 S S R X A |     | A D H / 0 H / 1 6 C | 0 C 1 C 2 C 3 C PA0/ADC0/OP3O0 |     | PIU2017  16 PA0 |     |     |     |
| --- | --- | --- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | ------------------------------ | ------------- | --- | ------------------- | ------------------------------ | --- | --------------- | --- | --- | --- |
COP6  PIC3501  PIC3601  PIU2060  S _ O I O I D A D A D A D A D A PIU2016
|     | P6  |     |     |     |     |     |     | PIN |     | 2.2uF | 0.1uF |     |     | C 3 S Q S Q S H | S H S H S H S H |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --------------- | --------------- | --- | --- | --- | --- | --- |
3V3 PIP601  1 2 PIP602  3V3 I / _ / _ 1 / _ 1 / 2 O / 0 / 1 / 2 / 3
P 3V3 F 6 PIP603  3 4 PIP604  P 3V3 F 7 1 K I S O O S I S 1 C 1 C 1 C 1 C A33DDV
P F 8 PIP605  5 6 PIP606  P F 9 GND KDDV 33DDV C S M I M Q /0 D A D A D A D A PFERV
P F 1 PIP607  0 7 8 PIP608  P C 0 SSV / 7 F / 8 F / 9 F 1 F IX O / 0 C / 1 C / 2 C / 3 C
P C 1 P I P 6 0 9   9 1 0 P I P 6 0 1 0   P C 2 COP9  P9 PIU200  PIU201 PIU202 PIU203 PIU204 PIU205 PIU206 PIU207 PIU208 PIU209 PIU2010 PIU2011 PIU2012 PIU2013 PIU2014 PIU2015  P P P P X P P P P
|     | P C 3 PI P 6 0 1 1   1 1 | 1 2 P I P 6 0 1 2   P A 0 |     |     | VREF |     | 3 V 3 |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------ | ------------------------- | --- | --- | ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P A 1 PIP6013  1 3 1 4 PIP6014  P A 2 V D D 3 PIP901  3 A 1 2 PIP902  3 V 3 0 1 2 3 4 5 6 7 8 9 0 1 1 1 2 1 3 1 41 51
P A 3 PIP6015  1 1 5 7 1 1 6 8 PIP6016  P A 4 V D D 3 PIP903  3 3 5 4 6 PIP904  3 V 3 KDDV 33DDV FERV A33DDV LED
P A 5 PIP6017  1 9 2 0 PIP6018  P A 6 3V3 PIP905  7 8 PIP906  3 V 3 6FP 7FP 8FP 9FP 01FP OX 0CP 1CP 2CP 3CP
|     | P A 7 PIP6019  PIP6021  2 1 | 2 2 PIP6020  PIP6022  P C 4 |     |     | GND | PIP907  PIP909  9 | 1 0 PIP908  PIP9010  GND |     |     |     |     |     |     | IX  |     |     |     |     |     |     |
| --- | --------------------------- | --------------------------- | --- | --- | --- | ----------------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | P C 5 PIP6023  2 3          | 2 4 PIP6024  P B 0          |     |     | GND | PIP9011  1 1      | 1 2 PIP9012  GND         |     |     |     |     | GND |     |     |     |     |     |     |     |     |
|     | P B 1 PIP6025  2 5          | 2 6 PIP6026  G N D          |     |     | GND | PIP9013  1 3      | 1 4 PIP9014  G N D       |     |     |     |     |     |     |     |     |     |     |     |     |     |
GND PIP6027  2 7 2 8 PIP6028  GND V V B B U U S S PIP9015  _ CC 1 5 1 6 PIP9016  G G N N D D COC4P5IC4502  COC4PIC64601  PIC4C202 OC42 PCIC4002 OC40  C45 C46 C42C40 PIC4C902 OC49 PIC5C102 OC51  C49 C51
|     |     |     |     |     |     | PIP9017  1 7 | 1 8 PIP9018  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
COP8  P8 0.1uF PIC4501  2.2uF PIC4602 PIC4201  0.1uF10uF PIC4001  PIC4901  0.1uF PIC5101  0.1uF
| G   | N D             | GND               |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | COLED1  L E D 1 |       |
| --- | --------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- |
| P   | F 1 2 PIP801  1 | 2 PIP802  P F 1 3 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | COR16  R 1 6 L  | E D 1 |
P E 9 PIP803  3 4 PIP804  P E 1 5 GND GND GND GND VDDIO PIR1601  1 k PIR1602 PILED101 PILED102
| P   | D 9 PIP805  5 7 | 6 8 PIP806  P D 1 0 |     |     |     | COP3  P3 |       |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------- | ------------------- | --- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P   | C 6 PIP807  9   | 1 0 PIP808  P C 7   |     |     | 3   | V 3 1    | 2 GND |     |     |     |     |     |     |     |     |     |     |     |     |     |
P C 8 P I P 8 0 9   1 1 1 2 P I P 8 0 1 0 P   C 9 G N D P I P 3 0 1   3 4 P I P 3 0 2 GND   COR18  R 1 8 COLED2  L E D 2
P A 1 1 PI PIP8013  P 8 0 1 1   1 3 1 4 P PIP8014  I P 8 0 1 2 P   A 1 2 P B 9 P PIP305  I P 3 0 3   5 6 P PIP306  I P 3 0 4 G   N D VDDIO PIR1801  PIR1802 PILED201 PILED202  L E D 2
D P A 1 3 PIP8015  1 5 1 6 PIP8016  P A 1 4 P B 8 PIP307  7 8 PIP308  G N D 1 k D
| P   | C 1 0 PIP8017  1 7     | 1 8 PIP8018  P C 1 1     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P P | C D 1 3 2 PIP8019  1 9 | 2 0 PIP8020  P P D B 3 2 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| P   | B 4 PIP8021  2 1       | 2 2 PIP8022  P B 5       |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| P   | B 6 PIP8023  2 3       | 2 4 PIP8024  P B 7       |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| L   | E D 1 PIP8025  2 5     | 2 6 PIP8026  L E D 2     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| K   | E Y PIP8027  2 7       | 2 8 PIP8028  GND         |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| G   | N D PIP8029  2 9       | 3 0 PIP8030  G N D       |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 3V3 | PIP8031  3 33 1        | 34 3 2 PIP8032  3V3      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | PIP8033                | PIP8034                  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | 1                      |                          |     |     | 2   |     |     |     | 3   |     | 4   |     |     | 5   |     |     | 6   | 7   |     | 8   |

|     | 1   |         |     | 2   |          |     | 3           |     | 4   |     |     | 5   |     |     | 6   |     |     | 7   |           | 8   |     |
| --- | --- | ------- | --- | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
|     |     |         |     |     |          |     | POWER&USBPD |     |     |     |     |     |     |     |     |     |     |     | POWER&USB |     |     |
|     |     | VBUS_CC |     |     | COL1  L1 |     | VBUS        |     |     |     |     |     |     |     |     |     |     |     |           |     |     |
PIC102 COC1  PIC202 COC2  PIL101  PIL10P2IC401 C   PIR302  5V COP4
|     |     | C 1 | C 2 | COC7  C7 | NC(4 .7 u H | /5 A )C4 OC4  COR3  |     |     |     |     |     |     |     |     |     |     |     | P4 0 |     |     |     |
| --- | --- | --- | --- | -------- | ----------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
NC(22uF/35 PIC101  V ) PIC201  N C(0.1uF) PIU1010 PIU109 PIU108 PIU107 PPIU1I06 C701   PIC702  R3 PIC3202 COC32 PIC3302 COC33  DNG
0 1 9 8 7 6 CO U1  NC(100nF) N C ( 6F8 pB F) PIC402  NC(15K PIR301  ) C32 C33 GND PIP404  4
U1 PIR802  PIC3201  PIC3301  NC(22uF) U D + P I P 3 4 0 3   OTG_FS_DP
A GND N N W W T COR8  RN8C(22uF) GND U D - P I P 1 2 4 0 2   OTG_FS_DM A
|     |     |     | I V | I V S S S B |     | NC(4.7K) |     |     |     |     |     |     |     |     |     |     |     | DNG +5V PIP401  |     |     |     |
| --- | --- | --- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- |
PIR801  PIR2802  C R O R2266  PINR260C1 (0Ω) VDDK PIP400  VBUS_FS
|     |     |     |                                                |                   |     |           |     |     |     |                   |                            |            |                    | 1V2 PIR26 0  | 2               |     |     |     |     |     |     |
| --- | --- | --- | ---------------------------------------------- | ----------------- | --- | --------- | --- | --- | --- | ----------------- | -------------------------- | ---------- | ------------------ | ------------ | --------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | D N                                            | D N               |     |           |     |     |     |                   | CR OR22                    | 8 8        |                    |              |                 |     |     | 0   |     |     |     |
|     |     |     | N I V                                          | . C . C B G       |     | GNDGNDGND |     |     |     |                   | PIR2801  N                 | C (200k)   | CUOU33             |              |                 |     |     |     |     |     |     |
|     |     |     | G PIU100 PIU101 PIU102 PIU103 PIU104 PIU105  A | N N F A           |     |           |     |     |     |                   | CCOC5566P IC5602  PIR2702  |            |                    |              |                 |     |     |     |     |     |     |
|     |     |     | 0 1 2                                          | 3 4 5 NC(CH2024Q) |     |           |     |     |     |                   | CROR227 7                  |            |                    |              |                 |     |     |     |     |     |     |
|     |     |     |                                                |                   |     |           |     |     |     | NC(4.7pF)PIC5601  | N C                        | ( 0 Ω )    | 10                 | 6            | CC OC 88        |     |     |     |     |     |     |
|     |     |     |                                                | BF                |     |           |     |     |     |                   | PIR2701 1V 2               | CL O L22   | P I U 3 2 1   N C. | F B P I5 U 3 | 0 6   3 V 3 1 0 | u F |     |     |     |     |     |
VBUS_CC PPIC57 02I  G N D P I U 3 3 0 2   G N D LDO _3 V 3 P I 4 U 3 0 5 PIC5302    PIC5402  P I C 8 0 2   PI C8 0 1  GND PIRCR 4O60R2 44 66 NC PIR4 6 01
COP1  P1 CC OLC 5 257 7 0  2 N   C (2 .2 uH ) PIL20 P1  I U 3 0 3  S W V IN 5 P I U 3 0 4 C  COC55 33  CCOC 55 4 5 4  V VBUS_FS UCOU66  ( 0 Ω)
B12B9 A1A4 A 1 VBUS_CC PIC5701 N P IC5301 1 uFPIC5401 10uF VBUS
G N D P I P A 1 4 0 A 1   C(10uF) PIU3603 V O - P I U2 6 0 2   P I C 5 8 0 1
|     |     | V B U S P I P B 1 8 0 A | 4   C OR 1  |     |     |     |     |     |     |     |     |     | CH2003V |     |     |     |     |   V I+ | 16  |     |     |
| --- | --- | ----------------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------ | --- | --- | --- |
R F U 1 P I P A 1 5 0 B 8 C   C 1_ 1 R1 0Ω CC1 G N D P I U 0 1   P I C 5 8 0 2  C COC 558 8
CC2 C R13 OR13  C C P I P B 1 7 0 A 5 U   SB PIR10 H S_DM 2   PIR101  GN D G N D C H 2 13 1 0 u F
|     | PIR130 1  N C (5.1K) PIR1302  | D D + - P I P A 1 6 0 B | 7 U   S B H S _ D P | VBUS_CC | COP10  P10 |     | VBUS |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------------------------- | ----------------------- | ------------------- | ------- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | C R1 OR12  2                  | D - PIP10A6  A 7        | U S B H S _ D M     |         | 1          | 2   |      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
CC1 PIR120 1  PIR1202  D + P P I I P P B 1 1 6 0 0 A B 7 6 U     S B H S _ D P P P I I P P 1 1 0 0 0 0 1 3     3 4 P P I I P P 1 1 0 0 0 0 2 4     GND
|     | NC(5.1K) | R F U 1 PIP10A8  A 8            | COR9  R9                 |     | PIP1005  5 | 6 PIP1006  |     |     |     |     |     |     |     |                |                               |                    |     |     |                            |     |     |
| --- | -------- | ------------------------------- | ------------------------ | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------------------------- | ------------------ | --- | --- | -------------------------- | --- | --- |
|     |          | C C PIP10B5  B 5                | CC1_2 PIR902  PIR901  0Ω | CC2 |            |            |     |     |     |     |     |     |     |                |                               |                    |     |     |                            |     |     |
|     |          | A9A12 B4B1 V B U S PIP10B4  B 4 |                          |     | HEADER 3x2 |            |     |     |     |     |     |     |     |                |                               |                    |     |     |                            |     |     |
|     |          | G N D PIP10B1  B 1              | VBUS_CC                  |     | GND        | GND        |     |     |     |     |     |     |     |                |                               | GND                |     |     |                            |     |     |
|     |          | USBHS                           |                          |     |            |            |     |     |     |     |     |     |     |                |                               |                    |     |     |                            | MCU |     |
| B   |          |                                 |                          |     |            |            |     |     |     |     |     |     |     | PD_SF_GTO      | MD_SF_GTO                     | COC1PIC61602   C16 |     |     |                            |     | B   |
|     |          |                                 |                          |     |            |            |     |     |     |     |     |     |     |                |                               | 0.1uF PIC1601      |     |     | COR5  R5                   |     |     |
|     |          |                                 |                          |     |            |            |     |     |     |     |     |     |     |                |                               |                    |     | 3V3 | 0Ω VDD33                   |     |     |
|     |          |                                 |                          |     |            |            |     |     |     |     |     |     |     |                |                               | 31BP 21BP 33DDV    |     |     | PIR50C2O R10 PIR501  R100Ω |     |     |
|     |          |                                 |                          |     |            |            |     |     |     |     |     |     |     | 41AP 31AP 21AP | 11AP 01AP 9AP 9CP 8CP 7CP 6CP | 51BP 41BP          |     |     | PIR1002  PIR1001  VDD33A   |     |     |
PIU2045 PIU2044 PIU2043 PIU2042 PIU2041 PIU2040 PIU2039 PIU2038 PIU2037 PIU2036 PIU2035 PIU2034 PIU2033 PIU2032 PIU2031
|     |     |     |     |     |     |     |     | XTAL |     |     |     |     |     | 54 4 4 3 4 | 2 4 1 4 0 4 9 3 8 3 7 3 6 3 | 5 3 4 3 3 3 23 13 |     | COU2  U2 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---------- | --------------------------- | ----------------- | --- | -------- | --- | --- | --- |
CH32H415REU6
|     |     |     |                  |                  |     |     |     |     |     |     |     |     |     | 41AP 3 1 P D | M D S U 9 C 8 C 7 C | 6 C 5 1 4 1 3 1 21BP 33DDV |     |     |     |     |     |
| --- | --- | --- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------- | -------------------------- | --- | --- | --- | --- | --- |
|     |     |     | COC23  C23       |                  |     |     |     |     |     |     |     |     |     | A P _ G      | D _ I _ G B P P P   | P B P B P B P              |     |     |     |     |     |
|     |     |     |                  | XI               |     |     |     |     |     |     |     |     |     | T            | G T T O V _         |                            |     |     |     |     |     |
|     |     |     | PIC2301 PIC2302  | PIY201           |     |     |     |     |     |     |     |     |     | O / 2        | O / / 0 G T         |                            |     |     |     |     |     |
|     |     | GND | 18pF             | 1                |     |     |     |     |     |     |     |     |     | 1 A          | 1 1 A 1 A O / 9     |                            |     |     |     |     |     |
|     |     |     |                  | PIY203  COY2  Y2 |     |     |     |     |     |     |     |     |     | P            | P P A P             |                            |     |     |     |     |     |
COC25  C25 3 25M PA15 PIU2046  46 PA15 P B 1 1 PIU2030  3 0 PB11
PIC2501 PIC2502  XO PC10 PIU2047  4 7 P C 1 0 PB10/P E 1 5 / I 3 C _ S D A PIU2029  2 9 PE15PB10
18pF PC11 PIU2048  4 8 P C 1 1 P E 1 4 / I 3 C _ S C L PIU2028  2 8 PE14
|     |     |     |     |     |     |     |     |     |     |     |     | PC12    | PIU2049  4 9 P C 1 2   |     |     |                         | P E 1 3 PIU2027  2 7     | PE13      |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------------- | --- | --- | ----------------------- | ------------------------ | --------- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |     | PD3 PF3 | PIU2050  5 5 0 1 P D 3 |     |     |                         | P E 1 2 PIU2026  2 2 6 5 | PE12 PE11 |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     | PF4     | PIU2051  5 2 P F 3     |     |     |                         | P E 1 1 PIU2025  24      | PB1       |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     | PF5     | PIU2052  5 3 P F 4     |     |     | PB1/ADC9/OP1_N0/CMP_N0  | PIU2024  23              | PB0       |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     | PE0     | PIU2053  5 4 P F 5     |     |     | PB0/ADC8/OP1_P0/CMP_P0  | PIU2023  22              | PC4       |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     | PB3     | CC1 PIU2054  5 5 P E 0 |     |     | PC4/ADC14/OP1_O0/CMP_N1 | PIU2022  2 1             | PA7       |     |     |     |
KEY COR16  COLED1  LED1 LED PB4 CC2 P I U 2 5 0 6 5 5   P P B B 4 3 / / C C C C 2 1 0 P P A A 7 6 / / A A D D C C 7 6 / / O O P P 1 1 _ _ N P 1 1 P I U 2 2 0 0 2 1   PA6
C 3V3 VDD33 R16 LED1 PB6 P I U 2 5 0 7 5 6   P B 6 0 P _ N _ P A 5 / A D C 5 / O P 1 _ O 1 / D A C 2 P I U 1 2 9 0 2 0   PA5 C
PIR1701  PIR1601  1k PIR1602 PILED101 PILED102  PB7 PIU2057  5 8 P B 7 3 P 3 P P A 4 / A D C 4 / O P 3 _ O 1 / D A C 1 PIU2019  1 8 PA4
COR17  PB8 USBHS_DP PIU2058  PIU2059  5 9 P B 8 / U S B 2 D P /S W C L K O / O / P A 3 / A D C 3 / O P 3 _ N 1 PIU2018  PIU2017  1 7 PA3
R17 COLED2  PB9 USBHS_DM PIU2060  6 0 P B 9 / U S B 2 D M /S W D I O 0 C D 1 C 2 C D 3 C D 0O_3PO/0CDA/0AP PA2/ADC2/OP3_P1 PIU2016  16 PA2
|     | PIR1702  10K |     |     |     |     |     | COR18  R18 LED2 |     |     |     |     |     |     |     | A   | D A A A |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
KEY PIS20C1OS 2  1 1 2 PIS202  2 GND VDD33 PIR1801  PIR1802 PILED201 PILED202  LED2 S H S H S H S H
|     |          | S2 USER |     |     |     |     | 1k  |     |     |     |     |     |     |     | / 0 1        | / 1 1 / 2 1 / 3 1 1CDA/1AP |     |     |     |     |     |
| --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------------------- | --- | --- | --- | --- | --- |
|     |          |         |     |     |     |     |     |     |     |     |     |     |     |     | C D          | C D C D C D A              |     |     |     |     |     |
|     | COP6  P6 |         |     |     |     |     |     |     |     |     |     |     |     |     | KDDV 33DDV A | A A A 3 3D                 |     |     |     |     |     |
3V3 3V3 PIN SSV 3EP 4 E 5 E 6EP I O / 0 C / 1 C / 2 C / 3 C D
PB15 PIP601  1 2 PIP602  GND PIU200  PIU201 PIU202 PIU203 PIU204 PIU205 PIU206 PIU207 PIU208 PIU209 PIU2010 PIU2011 PIU2012 PIU2013 PIU2014 PIU2015  P P X X P P P P V
|     | PB13 PIP603  3 5 4 6 | PIP604  PB14 |     |     |     |     | COP9  P9 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------- | ------------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PB11 PIP605  7 8 PIP606  PB12 VDD33A 1 2 3V3 0 1 2 3 4 5 6 7 8 9 0 1 1 1 2 1 3 1 41 51
PE15 PIP607  PIP609  9 1 0 PIP608  PIP6010  PB10 COP5  VDD33 PIP901  PIP903  3 4 PIP902  PIP904  3V3 A33DDV
PE13 PIP6011  11 1 2 PIP6012  PE14 P5 GND PIP905  5 6 PIP906  GND 3EP 4EP 5EP 6EP KDDV 33DDV OX 0CP 1CP 2CP 3CP
PE11 PIP6013  13 14 PIP6014  PE12 KEY PIP501  1 2 PIP502  PB7 VBUS PIP907  7 8 PIP908  GND IX 0AP 1AP
PB0 PIP6015  15 16 PIP6016  PB1 PB6 PB3 PIP503  3 4 PIP504  PB4 PE0 VBUS_CC PIP909  9 10 PIP9010  GND GND
|     | HEADER 8x2 |     |     | PF5 PIP505  5  | 6 PIP506  PF4    |     | HEADER 5x2 |     |     |     |     |     |     |                                                              |            |                    |     |     |     |     |     |
| --- | ---------- | --- | --- | -------------- | ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | ---------- | ------------------ | --- | --- | --- | --- | --- |
|     |            |     |     | PF3 PIP507  7  | 8 PIP508  PD3    |     |            |     |     |     |     |     |     | COC4PIC54502  COC4PIC64601  PCIC4202 OC42 PIC4C002 OC40  C45 | C46 C42C40 | COC5PIC15102   C51 |     |     |     |     |     |
|     |            |     |     | PC12 PIP509  9 | 10 PIP5010  PC11 |     |            |     |     |     |     |     |     |                                                              |            |                    |     |     |     |     |     |
COP8  P8 PC10 PIP5011  1 1 1 2 PIP5012  PA15 0.1uF PIC4501  2.2uF PIC4602 PIC4201  0.1uF4.7uF PIC4001  0.1uF PIC5101
|     | GND                 | PC4         |     | PA14 PIP5013  1 3   | 1 4 PIP5014  PA13   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------- | ----------- | --- | ------------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | PA7 PIP801  1 3 2 4 | PIP802  PA6 |     | PA12 PIP5015  15 17 | 16 18 PIP5016  PA11 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
PA5 PIP803  5 6 PIP804  PA4 PA10 PIP5017  19 20 PIP5018  PA9 GND GND GND
|     | PA3 PIP805  7 8          | PIP806  PA2          |     | PC8 PIP5019  21          | 22 PIP5020  PC9          |     | COP3  P3                    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------ | -------------------- | --- | ------------------------ | ------------------------ | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | PA1 PIP807  PIP809  9 10 | PIP808  PIP8010  PA0 |     | PC6 PIP5021  PIP5023  23 | 24 PIP5022  PIP5024  PC7 |     | 3V3 PIP301  1 2 PIP302  GND |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
D PC3 PIP8011  11 12 PIP8012  PC2 GND PIP303  3 4 PIP304  GND D
|     | PC1 PIP8013  13 14     | PIP8014  PC0     |     |     |     |     | PB9 PIP305  5 6 PIP306  GND |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------- | ---------------- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | PE6 PE4 PIP8015  15 16 | PIP8016  PE5 PE3 |     |     |     |     | PB8 PIP307  7 8 PIP308  GND |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | LED1 PIP8017  17 18    | PIP8018  LED2    |     |     |     |     |                             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | GND PIP8019  19 20     | PIP8020  GND     |     |     |     |     |                             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | 3V3 PIP8021  21 22     | PIP8022  3V3     |     |     |     |     |                             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | PIP8023  23 24         | PIP8024          |     |     |     |     |                             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     | 1                      |                  |     | 2   |     |     | 3                           |     | 4   |     |     | 5   |     |     | 6   |     |     | 7   |     | 8   |     |
