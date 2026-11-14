# Power

Any one of the three USB-C ports powers the whole board. The RP2354B is always powered; the CH32 and everything
that only talks to it sit in a switched domain that the RP can turn off — power-cycling the CH32 is also how its
bootloader is entered.

```
VBUS1 (J1) ─ LM66100 ─┐
VBUS2 (J2) ─ LM66100 ─┼─ VSYS +5V ─ TLV62569 buck ─ +3V3 (always on) ─┬─ RP2354B (+ internal 1.1 V SMPS)
VBUS3 (J3) ─ LM66100 ─┘                                               ├─ Si5351A, TS3USB221A, SAO J7, LED D6
                                                                      └─ TPS22918 load switch (RP GPIO38, default ON)
                                                                           └─ +3V3_CH ─┬─ CH32H417 VDD33 / VDDIO / VIO18
                                                                                       ├─ ferrite ─ +3V3A_CH (VDD33A)
                                                                                       ├─ microSD, ADC10065
                                                                                       └─ capture switches U11–U13, LED D7
```

## Rails

| Rail | Source | Loads | Notes |
|---|---|---|---|
| VBUS1–3 | USB-C J1, J2, J3 | ideal diodes | 5.1 kΩ Rd on every CC pin: default 5 V from any source |
| +5V_SYS | 3 × LM66100 ideal diodes (U5–U7) | buck input | no port can back-feed another (D41: no external input) |
| +3V3 | TLV62569 buck (U8), 2.2 µH | RP2354B, Si5351A, TS3USB221A, J7, D6 | always on; 100k / 22k divider → 3.327 V (D68) |
| +1V1 | RP2354B internal SMPS (L2 3.3 µH) | RP2354B core | per the RP2350 hardware design guide |
| +3V3_CH | TPS22918 (U9), quick output discharge | CH32, microSD, ADC10065, capture switches, D7 | RP GPIO38 `CH_PWR_EN`, 100k pull-up → ON by default (D15) |
| +3V3A_CH | ferrite FB1 from +3V3_CH | CH32 VDD33A (ADC/HSADC) | no LDO (D39); HSADC wants VDDA ≥ 3.0 V |
| VDDK, VDD12A | CH32 internal LDO | CH32 core, USB3 PHY | no external 1V2 (D25) |

## CH32 power budget (estimate)

DS V1.9 Tables 3-6-4/3-6-5: I<sub>DDK</sub> ≈ 112 mA (400/100 MHz, all peripherals) + I<sub>DD12A</sub> ≈ 85 mA (USB3)
→ ≈ 0.4 W in the internal LDO, ≈ 0.75 W for the chip, roughly +20–25 °C over ambient with the exposed pad
stitched to the GND planes. **An estimate — to measure on hardware at full USB3 load.**

## Back-feed protection (D29)

The RP is always powered, so the only back-feed direction is RP → CH32 when the CH32 domain is off. Rev A uses no
bus-isolation ICs:

- RP firmware tri-states every line to the CH32 and disables the Si5351 outputs **before** switching the CH32 domain off.
- Every RP↔CH32 and clock line has a series resistor to limit clamp current if the firmware gets it wrong.
- I2C pull-ups for the CH32 bus sit on the CH32 rail; NRST is driven open-drain through 1 kΩ.
- PB8/PB9 are isolated by the TS3USB221A; the capture switches are powered from the CH32 domain and isolate with I<sub>off</sub>.
- LED D7 has its anode on +3V3_CH; the J6 HSADC inputs have 100 Ω in series.
- The RP's ADC watches +3V3_CH and VSYS (D28): the CH32 rail must read ≈ 0 V when off.

## Planes

In3 is split: +3V3_CH under the top 44 mm (CH32 half of the board), +3V3 below. In1 and In4 are GND planes, and
F.Cu / B.Cu carry GND pours. See [layout](layout.md).
