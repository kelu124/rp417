#!/usr/bin/python3
"""rp417 rev A schematic generator. Source of truth for the netlist.

Run:  /usr/bin/python3 hw/gen/build.py      (writes hw/rp417*.kicad_sch)
Design refs: .claude/SPEC.md, .claude/DECISIONS.md D01-D48, docs/design/block-diagram.html.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kisch import Sym, Part, Sheet, write_root, make_ic_symbol, HW, U

PROJECT = "rp417"

# ---------------------------------------------------------------- custom symbols
ADC_PINS = [("1", "CLK", "input", "L"), ("13", "VIN+", "input", "L"), ("12", "VIN-", "input", "L"),
            ("4", "VCOM", "passive", "L"), ("6", "VREF", "passive", "L"), ("7", "VREFT", "passive", "L"),
            ("8", "VREFB", "passive", "L"), ("5", "IRS", "input", "L"), ("15", "DF", "input", "L"),
            ("28", "STBY", "input", "L"), ("2", "VDDA", "power_in", "L"), ("9", "VDDA", "power_in", "L"),
            ("10", "VDDA", "power_in", "L"), ("3", "VSSA", "power_in", "L"), ("11", "VSSA", "power_in", "L"),
            ("14", "VSSA", "power_in", "L"),
            ("16", "D0", "output", "R"), ("17", "D1", "output", "R"), ("18", "D2", "output", "R"),
            ("19", "D3", "output", "R"), ("20", "D4", "output", "R"), ("23", "D5", "output", "R"),
            ("24", "D6", "output", "R"), ("25", "D7", "output", "R"), ("26", "D8", "output", "R"),
            ("27", "D9", "output", "R"), ("22", "VDDIO", "power_in", "R"), ("21", "VSSIO", "power_in", "R")]
lib = "(kicad_symbol_lib (version 20251024) (generator \"rp417-gen\")\n" + \
      make_ic_symbol("ADC10065", ADC_PINS) + "\n)\n"
open(os.path.join(HW, "lib", "rp417.kicad_sym"), "w").write(lib)

# ---------------------------------------------------------------- symbols
S = {k: Sym(*v) for k, v in {
    "CBT": ("lcsc", "SN74CBTLV3257PWR"), "RGB": ("lcsc", "NH-B2020RGBA-HF"),
    "R": ("Device", "R"), "C": ("Device", "C"), "L": ("Device", "L"), "FB": ("Device", "FerriteBead_Small"),
    "PWR_FLAG": ("power", "PWR_FLAG"), "HOLE": ("Mechanical", "MountingHole"),
    "CH32": ("lcsc", "CH32H417MEU6_C54973456"), "RP": ("lcsc", "RP2354B_C39843328"),
    "SI5351": ("lcsc", "SI5351A-B-GTR"), "TS3": ("lcsc", "TS3USB221ARSER"),
    "XTAL": ("lcsc", "X322512MMB4SI"), "SW": ("lcsc", "TS-1187A-B-A-B"),
    "RCLAMP": ("lcsc", "RClamp0524PATCT"), "TPS22918": ("lcsc", "TPS22918DBVR"),
    "USBC24": ("lcsc", "TYPE-C24PQT"), "USBC16": ("lcsc", "TYPE-C16PIN2MD"), "TF": ("lcsc", "TF-01A"),
    "LM66100": ("Power_Management", "LM66100DCK", {"6": "passive"}), "TLV": ("Regulator_Switching", "TLV62568DBV"),
    "USBLC6": ("Power_Protection", "USBLC6-2P6"), "BAT54S": ("Diode", "BAT54S"),
    "JP3": ("Jumper", "SolderJumper_3_Bridged12"), "HDR2X2": ("Connector_Generic", "Conn_02x02_Odd_Even"), "HDR2X3": ("Connector_Generic", "Conn_02x03_Odd_Even"), "HDR4": ("Connector_Generic", "Conn_01x04"),
    "ADC": ("rp417", "ADC10065"),
}.items()}

FP = {"R0402": "Resistor_SMD:R_0402_1005Metric", "C0402": "Capacitor_SMD:C_0402_1005Metric",
      "C0603": "Capacitor_SMD:C_0603_1608Metric", "C0805": "Capacitor_SMD:C_0805_2012Metric",
      "L0603": "Inductor_SMD:L_0603_1608Metric", "L1008": "Inductor_SMD:L_1008_2520Metric"}

sheets = {}
cur = None


def sheet(key, name, paper):
    global cur
    cur = sheets[key] = Sheet(name, f"{PROJECT}_{key}.kicad_sch", paper)


counter = {}


def nref(prefix):
    counter[prefix] = counter.get(prefix, 0) + 1
    return f"{prefix}{counter[prefix]}"


# D68: JLC part numbers for standard passives (basic unless noted; checked 2026-11-14 via jlcsearch/LCSC).
# Resistors 0402 1% thick film; caps X5R/X7R (C0G for pF), >=10 V on the VBUS/5 V rails.
LCSC_STD = {
    ("R0402", "0"): "C17168", ("R0402", "22"): "C25092", ("R0402", "27"): "C25100",   # 27R extended
    ("R0402", "33"): "C25105", ("R0402", "49.9"): "C25120", ("R0402", "100"): "C25076",
    ("R0402", "220"): "C25091", ("R0402", "330"): "C25104", ("R0402", "1k"): "C11702",
    ("R0402", "4.7k"): "C25900", ("R0402", "5.1k"): "C25905", ("R0402", "10k"): "C25744",
    ("R0402", "22k"): "C25768", ("R0402", "47k"): "C25792", ("R0402", "56k"): "C25796",  # 56k preferred
    ("R0402", "100k"): "C25741",
    ("C0402", "15p"): "C1548", ("C0402", "18p"): "C1549", ("C0402", "68p"): "C14441",       # 68p preferred
    ("C0402", "220p"): "C1513258",                                                       # extended, C0G
    ("C0402", "1n"): "C1523", ("C0402", "100n"): "C307331", ("C0402", "1u"): "C52923",     # 1u 25 V
    ("C0402", "2.2u"): "C12530", ("C0603", "4.7u"): "C19666", ("C0603", "10u"): "C96446",  # 10u 25 V
    ("C0805", "22u"): "C45783",
}
FP_KEY = {v: k for k, v in FP.items()}


def two(sym, prefix, value, fp, a, b, lcsc="", dnp=False, mpn=""):
    if not lcsc:
        lcsc = LCSC_STD.get((FP_KEY.get(fp), value), "")
    return cur.add(Part(nref(prefix), S[sym], value, fp, {"1": a, "2": b}, lcsc=lcsc, dnp=dnp, mpn=mpn))


def R(v, a, b, fp="R0402", **k): return two("R", "R", v, FP[fp], a, b, **k)


def C(v, a, b="GND", fp=None, **k):
    if fp is None:
        fp = "C0805" if v in ("22u",) else ("C0603" if v in ("10u", "4.7u") else "C0402")
    return two("C", "C", v, FP[fp], a, b, **k)


def Lx(v, a, b, fp="L0603", **k): return two("L", "L", v, FP.get(fp, fp), a, b, **k)


def flag(net):
    cur.add(Part(nref("#FLG"), S["PWR_FLAG"], "PWR_FLAG", "", {"1": net}))


def ic(ref, sym, value, fp, by_name=None, by_num=None, rest="error", lcsc="", dnp=False, mpn=""):
    s = S[sym]
    conns = {}
    for name, net in (by_name or {}).items():
        ps = s.pin_by_name(name)
        if not ps:
            raise KeyError(f"{ref}: no pin named {name}")
        for p in ps:
            conns[p[0]] = net
    for num, net in (by_num or {}).items():
        conns[num] = net
    for p in s.pins:
        if p[0] not in conns:
            if rest == "error":
                raise ValueError(f"{ref}: pin {p[0]} {p[1]} unassigned")
            conns[p[0]] = rest
    return cur.add(Part(ref, s, value, fp, conns, lcsc=lcsc, dnp=dnp, mpn=mpn))


# =================================================================== 1. POWER
sheet("power", "Power", "A3")
for i in (1, 2, 3):
    ic(f"U{4 + i}", "LM66100", "LM66100DCKR", "Package_TO_SOT_SMD:SOT-363_SC-70-6",
       by_name={"VIN": f"VBUS{i}", "VOUT": "+5V_SYS", "GND": "GND", "~{CE}": "GND", "ST": None, "NC": None},
       lcsc="C2869734")
    C("1u", f"VBUS{i}")
    flag(f"VBUS{i}")
C("10u", "+5V_SYS")
# 3V3 buck, always on (D25): Vout = 0.6 * (1 + 100k/22.1k) = 3.31 V
ic("U8", "TLV", "TLV62569DBVR", "Package_TO_SOT_SMD:SOT-23-5",
   by_name={"VIN": "+5V_SYS", "EN": "+5V_SYS", "GND": "GND", "SW": "BUCK_SW", "FB": "BUCK_FB"}, lcsc="C141836")
C("10u", "+5V_SYS")
Lx("2.2u", "BUCK_SW", "+3V3", fp="L1008", lcsc="C576403", mpn="DFE252012F-2R2M=P2")
R("100k", "+3V3", "BUCK_FB")
R("22k", "BUCK_FB", "GND")                       # D68: 22k basic (was 22.1k) -> 3.327 V
C("22u", "+3V3")
C("22u", "+3V3")
# CH32 domain load switch (D25, D15 default ON via pull-up)
ic("U9", "TPS22918", "TPS22918DBVR", "Package_TO_SOT_SMD:SOT-23-6",
   by_name={"VIN": "+3V3", "GND": "GND", "ON": "CH_PWR_EN", "CT": "LS_CT", "QOD": "+3V3_CH", "VOUT": "+3V3_CH"},
   lcsc="C131941")
R("100k", "+3V3", "CH_PWR_EN")
C("1n", "LS_CT")
C("1u", "+3V3")
C("10u", "+3V3_CH")
# analog rail (D39)
two("FB", "FB", "600R@100MHz", "Inductor_SMD:L_0603_1608Metric", "+3V3_CH", "+3V3A_CH", lcsc="C1002",
    mpn="GZ1608D601TF")
C("4.7u", "+3V3A_CH")
# RP ADC sense dividers (D28)
R("100k", "+3V3_CH", "ADC_V3V3CH")
R("100k", "ADC_V3V3CH", "GND")
C("100n", "ADC_V3V3CH")
R("100k", "+5V_SYS", "ADC_VSYS")
R("56k", "ADC_VSYS", "GND")
C("100n", "ADC_VSYS")
for n in ("GND", "+5V_SYS", "+3V3", "+3V3_CH", "+3V3A_CH"):
    flag(n)
for i in range(4):
    cur.add(Part(f"H{i + 1}", S["HOLE"], "M3", "MountingHole:MountingHole_3.2mm_M3", {})).in_bom = False

# =================================================================== 2. USB
sheet("usb", "USB + ESD", "A2")
# J1: USB-C 3.x, single orientation (D27): TX1/RX1 + D+/D- both rows, CC 5.1k
ic("J1", "USBC24", "TYPE-C 24P QT", "lcsc:USB-C-SMD_TYPE-C-24P-QT",
   by_name={"GND": "GND", "VBUS": "VBUS1", "CC1": "J1_CC1", "CC2": "J1_CC2", "D+": "J1_DP", "D-": "J1_DM",
            "SUB1": None, "SUB2": None, "TX1+": "SS_TX_P", "TX1-": "SS_TX_N", "RX1+": "SS_RX_P",
            "RX1-": "SS_RX_N", "TX2+": None, "TX2-": None, "RX2+": None, "RX2-": None, "EP": "GND"},
   lcsc="C2681555")
R("5.1k", "J1_CC1", "GND")
R("5.1k", "J1_CC2", "GND")
C("100n", "CH_SSTX_P", "SS_TX_P")   # device TX AC coupling
C("100n", "CH_SSTX_N", "SS_TX_N")
ic("D4", "RCLAMP", "RClamp0524PATCT", "lcsc:SLP2510P8_L2.5-W1.0-P0.50-BL",
   by_name={"IN1": "SS_TX_P", "IN2": "SS_TX_N", "IN3": "SS_RX_P", "IN4": "SS_RX_N", "GND": "GND", "NC": None},
   lcsc="C40960")
ic("D1", "USBLC6", "USBLC6-2SC6", "Package_TO_SOT_SMD:SOT-23-6",
   by_num={"1": "J1_DP", "6": "J1_DP", "3": "J1_DM", "4": "J1_DM", "2": "GND", "5": "VBUS1"}, lcsc="C7519")
# USB2 switch on PB8/PB9 (D14, D26): S=0 -> 1D (connector), S=1 -> 2D (RP SWD)
ic("U4", "TS3", "TS3USB221ARSER", "lcsc:UQFN-10_L2.0-W1.5-P0.50-BL",
   by_name={"1D+": "J1_DP", "1D-": "J1_DM", "2D+": "SWCLK_RP", "2D-": "SWIO_RP", "GND": "GND",
            "~{OE}": "GND", "D+": "CH_USBHS_DP", "D-": "CH_USBHS_DM", "S": "USB_SEL", "VCC": "+3V3"},
   lcsc="C128396")
R("100k", "USB_SEL", "GND")
C("100n", "+3V3")
# J2: CH32 USBFS (D40)
ic("J2", "USBC16", "TYPE-C 16PIN 2MD(073)", "lcsc:USB-C-SMD_TYPE-C-16PIN-2MD-073",
   by_name={"GND": "GND", "VBUS": "VBUS2", "CC1": "J2_CC1", "CC2": "J2_CC2", "Dp1": "J2_DP", "Dp2": "J2_DP",
            "Dn1": "J2_DM", "Dn2": "J2_DM", "SBU1": None, "SBU2": None, "EH": "GND"}, lcsc="C2765186")
R("5.1k", "J2_CC1", "GND")
R("5.1k", "J2_CC2", "GND")
ic("D2", "USBLC6", "USBLC6-2SC6", "Package_TO_SOT_SMD:SOT-23-6",
   by_num={"1": "J2_DP", "6": "J2_DP", "3": "J2_DM", "4": "J2_DM", "2": "GND", "5": "VBUS2"}, lcsc="C7519")
# J3: RP2350 USB, 27R series (RP2350 hardware design guide)
ic("J3", "USBC16", "TYPE-C 16PIN 2MD(073)", "lcsc:USB-C-SMD_TYPE-C-16PIN-2MD-073",
   by_name={"GND": "GND", "VBUS": "VBUS3", "CC1": "J3_CC1", "CC2": "J3_CC2", "Dp1": "J3_DP", "Dp2": "J3_DP",
            "Dn1": "J3_DM", "Dn2": "J3_DM", "SBU1": None, "SBU2": None, "EH": "GND"}, lcsc="C2765186")
R("5.1k", "J3_CC1", "GND")
R("5.1k", "J3_CC2", "GND")
ic("D3", "USBLC6", "USBLC6-2SC6", "Package_TO_SOT_SMD:SOT-23-6",
   by_num={"1": "J3_DP", "6": "J3_DP", "3": "J3_DM", "4": "J3_DM", "2": "GND", "5": "VBUS3"}, lcsc="C7519")
R("27", "J3_DP", "RP_USB_DP")
R("27", "J3_DM", "RP_USB_DM")

# =================================================================== 3. CH32
sheet("ch32", "CH32H417", "A1")
ch = {
    # CH32H417MEU6 QFN88 (D54). power (D23: VIO18 = VDDIO = 3V3); no VREFP/VBAT/VSSA pins on QFN88
    "VDD33": "+3V3_CH", "VDDIO": "+3V3_CH", "VIO18": "+3V3_CH", "VDD33A": "+3V3A_CH", "EP": "GND",
    "VDDK": "VDDK", "VDD12A": "VDD12A",
    "XI": "CH_XI", "XO": "CH_XO", "NRST": "CH_NRST",
    # DVP, one pin set fed by the 2:1 capture switch (D55): ADC10065 or RP counter
    "PE0": "CAP_D0", "PE1": "CAP_D1", "PB13": "CAP_D2", "PE3": "CAP_D3", "PE4": "CAP_D4", "PF14": "CAP_D5",
    "PE5": "CAP_D6", "PE6": "CAP_D7", "PF4": "CAP_D8", "PF3": "CAP_D9", "PB12": "CAP_PCLK",
    "PF2": "CAP_PCLK",                 # TIM8_ETR (AF3): sample counter
    "PA4": "DVP_HSYNC", "PA5": "DVP_VSYNC",
    # RP<->CH32 logic bus, general GPIO (D03)
    "PD12": "LOGIC0", "PD13": "LOGIC1", "PD14": "LOGIC2", "PD15": "LOGIC3", "PD10": "LOGIC4", "PD11": "LOGIC5",
    "PC6": "LOGIC6", "PC7": "LOGIC7",
    "PC0": "CH_AIN0",
    "PC1": "CH_AIN1",                  # D65 HSADC_IN1 / ADC_IN11, on J6 via 100R
    "PC3": "CH_AIN3",                  # D64 HSADC_IN3 / ADC_IN13, on J6 via 100R
    "PC2": "LED_CH_R", "PF0": "LED_CH_G", "PF1": "LED_CH_B",   # D62/D63 status LED (pins 17, 45, 46)
    # microSD (D04), SDMMC_RM=00
    "PD2": "SD_CMD", "PC12": "SD_CLK", "PC8": "SD_D0", "PC9": "SD_D1", "PC10": "SD_D2", "PC11": "SD_D3",
    "PD0": "SD_CD",
    # QSPI2 master (D38)
    "PE10": "QSPI_SCK", "PE11": "QSPI_CS", "PE12": "QSPI_IO0", "PE13": "QSPI_IO1", "PE14": "QSPI_IO2",
    "PE15": "QSPI_IO3",
    "PA9": "CH_UART_TX", "PA10": "CH_UART_RX",   # USART1 = UART ISP pins on QFN88 (EVB ref.)
    "PB10": "CH_SCL", "PB11": "CH_SDA",
    "PB14": "CH_MARK",                 # TIM9_CH1 (AF2)
    "PB0": "CH_MCO",
    "PB8": "CH_USBHS_DP", "PB9": "CH_USBHS_DM", "PA11": "J2_DM", "PA12": "J2_DP",
    "SSTXA": "CH_SSTX_P", "SSTXB": "CH_SSTX_N", "SSRXA": "SS_RX_P", "SSRXB": "SS_RX_N",
}
ic("U1", "CH32", "CH32H417MEU6", "lcsc:QFN-88_L10.0-W10.0-P0.40-BL-EP7.7", by_name=ch, rest=None,
   lcsc="C54973456", mpn="CH32H417MEU6 (user-supplied, D43/D54)")
# decoupling per DS V1.9 1.4.3 (QFN88 pin counts)
for _ in range(3): C("100n", "+3V3_CH")          # VDD33 x3
C("10u", "+3V3_CH")
for _ in range(2): C("100n", "+3V3_CH")          # VDDIO x2
for _ in range(3): C("100n", "+3V3_CH")          # VIO18 x3
C("2.2u", "+3V3_CH", fp="C0402")
for _ in range(2): C("100n", "VDDK")
C("2.2u", "VDDK", fp="C0402")
C("100n", "VDD12A")
C("2.2u", "VDD12A", fp="C0402")
C("100n", "+3V3A_CH")
C("1u", "+3V3A_CH")
flag("VDDK")
flag("VDD12A")
# HSE 25 MHz, 12 pF load
ic("Y2", "XTAL", "25MHz 12pF", "lcsc:CRYSTAL-SMD_4P-L3.2-W2.5-BL",
   by_name={"OSC1": "CH_XI", "OSC2": "CH_XO", "GND": "GND"}, lcsc="C9006", mpn="X322525MOB4SI")
C("18p", "CH_XI")
C("18p", "CH_XO")
# reset
C("100n", "CH_NRST")
ic("SW2", "SW", "RESET", "lcsc:SW-SMD_4P-L5.1-W5.1-P3.70-LS6.5-TL_H1.5",
   by_name={"A": "CH_NRST", "B": "CH_NRST", "C": "GND", "D": "GND"}, lcsc="C318884")

# =================================================================== 4. RP2354B
sheet("rp", "RP2354B supervisor", "A1")
rp = {
    "IOVDD": "+3V3", "DVDD": "+1V1", "VREG_VIN": "+3V3", "VREG_AVDD": "RP_VREG_AVDD", "VREG_PGND": "GND",
    "VREG_LX": "RP_VREG_LX", "VREG_FB": "+1V1", "ADC_AVDD": "+3V3", "USB_OTP_VDD": "+3V3",
    "QSPI_IOVDD": "+3V3", "GND": "GND", "XIN": "RP_XIN", "XOUT": "RP_XOUT", "RUN": "RP_RUN",
    "USB_DM": "RP_USB_DM", "USB_DP": "RP_USB_DP", "QSPI_SS": "RP_QSPI_SS",
    "GPIO0": "RP_UART_TX", "GPIO1": "RP_UART_RX", "GPIO2": "RP_SDA", "GPIO3": "RP_SCL",
    "GPIO4": "MGMT_SDA", "GPIO5": "MGMT_SCL",
    "GPIO6": "QSPI_SCK_RP", "GPIO7": "QSPI_CS_RP", "GPIO8": "QSPI_IO0_RP", "GPIO9": "QSPI_IO1_RP",
    "GPIO10": "QSPI_IO2_RP", "GPIO11": "QSPI_IO3_RP",
    **{f"GPIO{12 + i}": f"LOGIC{i}_RP" for i in range(8)},          # GPIO12-19 logic bus
    **{f"GPIO{20 + i}": f"CNT_D{i}_RP" for i in range(10)},         # GPIO20-29 PIO counter D0-D9
    "GPIO30": "CNT_PCLK_RP",                                         # PIO side-set clock
    "GPIO42_ADC2": "CAP_SEL",                                        # 2:1 capture switch select
    "GPIO31": "HSYNC_RP", "GPIO32": "VSYNC_RP", "GPIO33": "MARK_RP", "GPIO34": "MCO_RP",
    "GPIO35": "SWIO_RP", "GPIO36": "SWCLK_RP", "GPIO37": "CH_NRST_RP", "GPIO38": "CH_PWR_EN",
    "GPIO39": "USB_SEL", "GPIO40_ADC0": "ADC_V3V3CH", "GPIO41_ADC1": "ADC_VSYS",
    "GPIO43_ADC3": "LED_RP_R", "GPIO46_ADC6": "LED_RP_G", "GPIO47_ADC7": "LED_RP_B",   # D62 status RGB (R moved to GPIO43, D66)
    "GPIO44_ADC4": "SAO_SDA", "GPIO45_ADC5": "SAO_SCL",                                 # D66 I2C0 on the SAO header
}
ic("U2", "RP", "RP2354B", "lcsc:QFN-80_L10.0-W10.0-P0.40-TL-EP3.4", by_name=rp, rest=None, lcsc="C39843328")
for _ in range(8): C("100n", "+3V3")             # IOVDD x8
for _ in range(3): C("100n", "+1V1")             # DVDD x3
C("4.7u", "+3V3")                                # VREG_VIN
R("33", "+3V3", "RP_VREG_AVDD")
C("4.7u", "RP_VREG_AVDD")
Lx("3.3u", "RP_VREG_LX", "+1V1", fp="Inductor_SMD:L_Abracon_AOTA-B201610S", lcsc="C42411119",
   mpn="AOTA-B201610S3R3-101-T")
C("4.7u", "+1V1")
for _ in range(3): C("100n", "+3V3")             # ADC_AVDD, USB_OTP_VDD, QSPI_IOVDD
flag("+1V1")
flag("RP_VREG_LX")
# 12 MHz crystal, 10 pF (D47), per RP2350 design guide: 1k series on XOUT, 15 pF loads
ic("Y3", "XTAL", "12MHz 10pF", "lcsc:CRYSTAL-SMD_4P-L3.2-W2.5-BL",
   by_name={"OSC1": "RP_XIN", "OSC2": "RP_XTAL2", "GND": "GND"}, lcsc="C50430", mpn="X322512MMB4SI")
R("1k", "RP_XOUT", "RP_XTAL2")
C("15p", "RP_XIN")
C("15p", "RP_XTAL2")
# RUN pull-up, BOOTSEL
R("10k", "+3V3", "RP_RUN")
C("100n", "RP_RUN")
R("1k", "RP_QSPI_SS", "RP_BOOTSEL")
ic("SW1", "SW", "BOOTSEL", "lcsc:SW-SMD_4P-L5.1-W5.1-P3.70-LS6.5-TL_H1.5",
   by_name={"A": "RP_BOOTSEL", "B": "RP_BOOTSEL", "C": "GND", "D": "GND"}, lcsc="C318884")
# management I2C pull-ups (Si5351)
R("4.7k", "+3V3", "MGMT_SDA")
R("4.7k", "+3V3", "MGMT_SCL")

# =================================================================== 5. CLOCKS + ANALOG
sheet("analog", "Clocks + analog + capture switch", "A2")
ic("U3", "SI5351", "SI5351A-B-GTR", "lcsc:MSOP-10_L3.0-W3.0-P0.50-LS5.0-BL",
   by_name={"VDD": "+3V3", "VDDO": "+3V3", "GND": "GND", "XA": "SI_XA", "XB": "SI_XB", "SCL": "MGMT_SCL",
            "SDA": "MGMT_SDA", "CLK0": "SI_CLK0", "CLK1": "SI_CLK1", "CLK2": "SI_CLK2"}, lcsc="C504891")
C("100n", "+3V3")
C("100n", "+3V3")
C("1u", "+3V3")
ic("Y1", "XTAL", "25MHz 10pF", "lcsc:CRYSTAL-SMD_4P-L3.2-W2.5-BL",
   by_name={"OSC1": "SI_XA", "OSC2": "SI_XB", "GND": "GND"}, lcsc="C70582", mpn="X322525MMB4SI")
R("33", "SI_CLK0", "ADC_CLK")      # D29 series R on clock lines
R("0", "SI_CLK1", "SI_PCLK")       # P4-1/D57: 0R, switch Ioff isolates
# generator (D33): 50R source, 5th-order Butterworth C-L-C-L-C, fc 30 MHz, 50R load
R("49.9", "SI_CLK2", "LPF_IN")
C("68p", "LPF_IN")
Lx("470n", "LPF_IN", "LPF_MID", lcsc="C113132", mpn="LQW18ANR47G00D")   # D68: 430n not stocked at JLC
C("220p", "LPF_MID")
Lx("470n", "LPF_MID", "GEN_OUT", lcsc="C113132", mpn="LQW18ANR47G00D")
C("68p", "GEN_OUT")
R("49.9", "GEN_OUT", "GND")
# input-select header (D34): 1 GEN, 2 ADC_IN, 3 EXT, 4 GND
ic("J5", "HDR4", "1x04 GEN/ADC_IN/EXT/GND", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical",
   by_num={"1": "GEN_OUT", "2": "ADC_IN", "3": "EXT_IN", "4": "GND"}, dnp=True)   # D68: 2.54 headers DNP
R("49.9", "EXT_IN", "GND")                       # external source termination
ic("D5", "BAT54S", "BAT54S", "Package_TO_SOT_SMD:SOT-23",
   by_name={"A": "GND", "K": "+3V3", "COM": "ADC_IN"}, lcsc="C8592")   # clamp to always-on rail
# ADC10065 path (D30, D33, D44): AC couple, bias to VCOM, VIN- = VCOM
R("100", "ADC_IN", "ADC_AC")
C("100n", "ADC_AC", "ADC_VINP")
R("4.7k", "ADC_VINP", "ADC_VCOM")
ic("U10", "ADC", "ADC10065CIMT", "Package_SO:TSSOP-28_4.4x9.7mm_P0.65mm",
   by_name={"CLK": "ADC_CLK", "VIN+": "ADC_VINP", "VIN-": "ADC_VCOM", "VCOM": "ADC_VCOM", "VREF": "ADC_VREF",
            "VREFT": "ADC_VREFT", "VREFB": "ADC_VREFB", "IRS": "ADC_IRS", "DF": "GND", "STBY": "GND",
            "VDDA": "+3V3A_CH", "VSSA": "GND", "VDDIO": "+3V3_CH", "VSSIO": "GND",
            **{f"D{i}": f"ADC_DO{i}" for i in range(10)}},
   lcsc="C1542621", dnp=True, mpn="ADC10065CIMT/NOPB (DNP, user-fitted, D42)")
for n in ("ADC_VCOM", "ADC_VREF", "ADC_VREFT", "ADC_VREFB"):
    C("100n", n)
for _ in range(3): C("100n", "+3V3A_CH")
C("4.7u", "+3V3A_CH")
C("100n", "+3V3_CH")
C("4.7u", "+3V3_CH")
for i in range(10):                              # series R at the ADC outputs
    R("22", f"ADC_DO{i}", f"ADC_D{i}")   # D57
# IRS: 3-way solder jumper, default 1-2 = VDDA = 2 Vpp (D44)
ic("JP1", "JP3", "IRS 2/1.5/1 Vpp", "Jumper:SolderJumper-3_P1.3mm_Bridged12_RoundedPad1.0x1.5mm",
   by_name={"A": "+3V3A_CH", "C": "ADC_IRS", "B": "GND"}).in_bom = False   # copper jumper, not a part
# CH32 ADC/HSADC feed (D35): series R, AC, mid-rail bias
R("100", "ADC_IN", "CH_AIN_AC")
C("100n", "CH_AIN_AC", "CH_AIN0")
R("10k", "+3V3A_CH", "CH_AIN0")
R("10k", "CH_AIN0", "GND")

# 2:1 capture switch (D55): S=0 -> B1 = ADC10065 + Si5351 PCLK (default), S=1 -> B2 = RP counter.
# Powered from the CH32 domain: Ioff isolates both sides when the CH32 is off (D29).
# channels grouped by CH32 pin location (D57): U11 top edge, U12 left edge, U13 bottom edge
order = ["D0", "D1", "D8", "D9", "D3", "D4", "D6", "D7", "D2", "D5", "PCLK", None]
cap_a = [f"CAP_{x}" if x else None for x in order]
cap_b1 = [(f"ADC_{x}" if x != "PCLK" else "SI_PCLK") if x else None for x in order]
cap_b2 = [f"CNT_{x}" if x else None for x in order]
for k in range(3):
    m = {"S": "CAP_SEL", "~{OE}": "GND", "GND": "GND", "VCC": "+3V3_CH"}
    for ch_ in range(4):
        i = 4 * k + ch_
        m[f"{ch_ + 1}A"], m[f"{ch_ + 1}B1"], m[f"{ch_ + 1}B2"] = cap_a[i], cap_b1[i], cap_b2[i]
    ic(f"U{11 + k}", "CBT", "SN74CBTLV3257PWR", "lcsc:TSSOP-16_L5.0-W4.4-P0.65-LS6.4-BL", by_name=m,
       lcsc="C7637")
    C("100n", "+3V3_CH")
R("100k", "CAP_SEL", "GND")                      # default = ADC10065

# =================================================================== 6. microSD + RP<->CH32 links
sheet("links", "microSD + RP-CH32 links", "A2")
ic("J4", "TF", "TF-01A", "lcsc:TF-SMD_TF-01A",
   by_num={"1": "SD_D2", "2": "SD_D3", "3": "SD_CMD", "4": "+3V3_CH", "5": "SD_CLK", "6": "GND", "7": "SD_D0",
           "8": "SD_D1", "9": "SD_CD", "10": "GND", "11": "GND", "12": "GND", "13": "GND"}, lcsc="C91145")
for n in ("SD_CMD", "SD_D0", "SD_D1", "SD_D2", "SD_D3", "SD_CD"):
    R("47k", "+3V3_CH", n)
C("10u", "+3V3_CH")
C("100n", "+3V3_CH")
# series R between RP and CH32 (D29). 33R = source termination for fast lines.
links = [("RP_UART_TX", "CH_UART_RX", "220"), ("CH_UART_TX", "RP_UART_RX", "220"),
         ("RP_SDA", "CH_SDA", "100"), ("RP_SCL", "CH_SCL", "100"),
         ("QSPI_SCK", "QSPI_SCK_RP", "33"), ("QSPI_CS", "QSPI_CS_RP", "33"),
         ("QSPI_IO0", "QSPI_IO0_RP", "33"), ("QSPI_IO1", "QSPI_IO1_RP", "33"),
         ("QSPI_IO2", "QSPI_IO2_RP", "33"), ("QSPI_IO3", "QSPI_IO3_RP", "33"),
         *[(f"LOGIC{i}_RP", f"LOGIC{i}", "33") for i in range(8)],
         *[(f"CNT_D{i}_RP", f"CNT_D{i}", "22") for i in range(10)], ("CNT_PCLK_RP", "CNT_PCLK", "22"),   # D57
         ("HSYNC_RP", "DVP_HSYNC", "33"), ("VSYNC_RP", "DVP_VSYNC", "33"),
         ("CH_MARK", "MARK_RP", "33"), ("CH_MCO", "MCO_RP", "33"),
         ("CH_NRST_RP", "CH_NRST", "1k")]
for a, b, v in links:
    R(v, a, b)
R("4.7k", "+3V3_CH", "CH_SDA")                   # I2C pull-ups on the CH32 rail (D29)
R("4.7k", "+3V3_CH", "CH_SCL")

# ---------------------------------------------------------------- D62 status RGB LEDs
# Appended last so no existing reference is renumbered (board is hand-routed, D61).
# NH-B2020RGBA-HF common anode: 1 = R-, 2 = B-, 3 = + (anode), 4 = G- (datasheets/NH-B2020RGBA-HF.pdf p.2).
# GPIO sinks; anode on the GPIO's own rail so an unpowered CH32 is never back-fed (D29).
LED_FP = "lcsc:LED-ARRAY-SMD_4P-L2.1-W2.1-TL_NH-B2020RGBA"
cur = sheets["rp"]
ic("D6", "RGB", "NH-B2020RGBA-HF", LED_FP, by_num={"3": "+3V3", "1": "LED_RP_RK", "4": "LED_RP_GK", "2": "LED_RP_BK"},
   lcsc="C2874116")
R("1k", "LED_RP_R", "LED_RP_RK")
R("1k", "LED_RP_G", "LED_RP_GK")
R("330", "LED_RP_B", "LED_RP_BK")
cur = sheets["ch32"]
ic("D7", "RGB", "NH-B2020RGBA-HF", LED_FP, by_num={"3": "+3V3_CH", "1": "LED_CH_RK", "4": "LED_CH_GK", "2": "LED_CH_BK"},
   lcsc="C2874116")                                 # blue on PF1 (D63)
R("1k", "LED_CH_R", "LED_CH_RK")
R("1k", "LED_CH_G", "LED_CH_GK")
R("330", "LED_CH_B", "LED_CH_BK")                  # D63, appended last -> R91

# ---------------------------------------------------------------- D64 HSADC test header
# J6 2x2 2.54 mm: 1 PC1 (HSADC_IN1, via 100R, D65) | 2 GND / 3 PC3 (HSADC_IN3, via 100R) | 4 GEN_OUT.
# Jumper 1-3 = HSADC_IN1 + IN3 tied; jumper 3-4 = raw generator into PC3; 1-2 = IN1 grounded.
cur = sheets["analog"]
ic("J6", "HDR2X2", "2x02 AIN1/GND/AIN3/GEN", "Connector_PinHeader_2.54mm:PinHeader_2x02_P2.54mm_Vertical",
   by_num={"1": "AIN1_HDR", "2": "GND", "3": "AIN3_HDR", "4": "GEN_OUT"}, dnp=True)
R("100", "AIN3_HDR", "CH_AIN3")                   # limits back-feed into PC3 with the CH32 off (D29) -> R92
R("100", "AIN1_HDR", "CH_AIN1")                   # D65, same for PC1 -> R93

# ---------------------------------------------------------------- D66 SAO header (I2C0)
# "Shitty Add-On" v1.69bis 2x3 2.54 mm: 1 VCC | 2 GND / 3 SDA | 4 SCL / 5 GPIO1 | 6 GPIO2.
# RP2350 I2C0 = GPIO44 SDA / GPIO45 SCL. VCC = +3V3 (always-on RP rail, pull-ups on the same rail).
# GPIO1/GPIO2 not connected: no free RP GPIO left (SWD and QSPI pins excluded).
cur = sheets["rp"]
ic("J7", "HDR2X3", "SAO 2x03 VCC/GND/SDA/SCL", "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical",
   by_num={"1": "+3V3", "2": "GND", "3": "SAO_SDA", "4": "SAO_SCL", "5": None, "6": None}, dnp=True)
R("4.7k", "+3V3", "SAO_SDA")                      # -> R94
R("4.7k", "+3V3", "SAO_SCL")                      # -> R95

# ---------------------------------------------------------------- write + checks
order = ["power", "usb", "ch32", "rp", "analog", "links"]
root = U()
nets = {}
for k in order:
    sh = sheets[k]
    for p in sh.parts:
        for pin, net in p.conns.items():
            if net:
                nets.setdefault(net, []).append(f"{p.ref}.{pin}")
single = {n: v for n, v in nets.items() if len(v) < 2}
if single:
    raise SystemExit(f"single-pin nets (wiring error): {single}")
for k in order:
    sheets[k].write(HW, root, PROJECT)
write_root(HW, PROJECT, [sheets[k] for k in order], root,
           notes=["rp417 rev A draft - generated by hw/gen/build.py",
                  "Decisions D01-D48: see .claude/DECISIONS.md / .claude/SPEC.md / docs/design/block-diagram.html",
                  "U1 CH32H417QEU6 user-supplied (D43); U10 ADC10065 DNP, user-fitted (D42)"])
json.dump({k: sorted(v) for k, v in nets.items()}, open(os.path.join(HW, "gen", "nets.json"), "w"), indent=0)
print(f"parts: {sum(len(sheets[k].parts) for k in order)}  nets: {len(nets)}")
