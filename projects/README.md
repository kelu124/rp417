# CH32H417 reference projects

Open projects on GitHub that use the CH32H417 (or are tools we need for it), kept here so we can
grep schematics, pinouts and firmware while designing our board.

- `repos.txt` — the list that gets cloned (category + `owner/repo`)
- `clone.sh` — shallow-clones / updates everything into `projects/<category>/<repo>/`
- The clones themselves are **gitignored**; run `projects/clone.sh` after a fresh checkout.

Survey date: 2026-11-12 (GitHub search "ch32h417 / ch32h416 / ch32h415" + known repos).
★ = most relevant to rp417.

## Hardware (schematics / PCB)

| Repo | What | Why it matters to us |
|------|------|----------------------|
| ★ [vllogic/USB3.0_CH32H417_H7P20_dev_board](https://github.com/vllogic/USB3.0_CH32H417_H7P20_dev_board) | CH32H417 + HME H7P20 FPGA USB3 board, 400 MB/s+ one way | USB3 layout, parallel bus to FPGA, measured throughput |
| ★ [cheyao/ch32-logic-analyzer](https://github.com/cheyao/ch32-logic-analyzer) | 200 MHz USB3 logic analyzer + 20 MHz ADC, PulseView | Fast parallel capture + HSADC use, very close to our goals |
| ★ [WeActStudio/WeActStudio.LogicAnalyzerV2](https://github.com/WeActStudio/WeActStudio.LogicAnalyzerV2) | WeAct LA V2 (16 ch, 200 MHz, USB3) | Capture-pin mapping (UHSIF/DVP?) |
| [TriEverthing/CH32H417Q_DevBrd](https://github.com/TriEverthing/CH32H417Q_DevBrd) | QFN128 dev board | Same package as ours |
| [Calvariaa/CH32H417_Logic_Analyzer_Mini](https://github.com/Calvariaa/CH32H417_Logic_Analyzer_Mini) | 16 ch 200 MHz LA on WEU6 (QFN68), redrawn PCB | LA reference |
| [Doukeyi-X/OpenSourceLogic-CH32H417](https://github.com/Doukeyi-X/OpenSourceLogic-CH32H417) | Open-source 16 ch USB3 LA | LA reference |
| [marxing/CH32H417_LogicAnalyzer](https://github.com/marxing/CH32H417_LogicAnalyzer) | USB3 LA + dual-channel ADC, TFT, Type-C orientation detection | ADC front-end, USB-C orientation |
| [DeqingSun/CH32H417-logic-analyzer-pulseview](https://github.com/DeqingSun/CH32H417-logic-analyzer-pulseview) | PulseView port of the oshwhub q2h2 LA | Host side |
| [IvanLi-CN/ch32h417weu6-logic-analyzer](https://github.com/IvanLi-CN/ch32h417weu6-logic-analyzer) | WEU6 logic analyzer | LA reference |
| [MichealIbrahim/Communication-Board-CH32H417](https://github.com/MichealIbrahim/Communication-Board-CH32H417) | Ethernet/USB/CAN/RS485/microSD board | microSD wiring |
| [Kyin-code/CH32H417-Vibe-hardware](https://github.com/Kyin-code/CH32H417-Vibe-hardware) | Hardware project | — |
| [chcbaram/nano-ch32h417](https://github.com/chcbaram/nano-ch32h417) | Nano-style board | Small-form reference |
| [Funtaser/ch32h417-pins](https://github.com/Funtaser/ch32h417-pins) | Pin data | Pin planning |

## Vendor SDK / libraries

| Repo | What |
|------|------|
| ★ [openwch/ch32h417](https://github.com/openwch/ch32h417) | Official WCH EVT: examples (USBSS, UHSIF, DVP, HSADC, IAP…), EVB schematics |
| [ch32-riscv-ug/CH32H417](https://github.com/ch32-riscv-ug/CH32H417) | Community mirror/collection (large) |
| [makergo1024/CH32H417](https://github.com/makergo1024/CH32H417) | EVT examples with English docs |
| [zyitom/ch32h417-evt](https://github.com/zyitom/ch32h417-evt) | EVT subset + USBSS device stack, vendored |
| [maxgerhardt/ch32h417lib](https://github.com/maxgerhardt/ch32h417lib) | No-OS peripheral lib vendored for MicroPython |
| [SoCXin/CH32H417](https://github.com/SoCXin/CH32H417) | Early docs collection |

## Firmware (USB3 streaming, bring-up, build systems)

| Repo | What |
|------|------|
| ★ [Liren66/OmniCore-SDR-Firmware](https://github.com/Liren66/OmniCore-SDR-Firmware) | Zynq/AD9361 SDR with CH32H417 USB3 dual-core bridge — sustained streaming |
| [mfkiwl/OmniCore-SDR-Bridge](https://github.com/mfkiwl/OmniCore-SDR-Bridge) | USB3 bridge firmware (CH32H417) |
| [czstara12/U3LogicAnalyzer](https://github.com/czstara12/U3LogicAnalyzer) | LA host tool: cross-platform build, decoding |
| [OpenChipLab/CH32H417-sigrok-cli](https://github.com/OpenChipLab/CH32H417-sigrok-cli) | sigrok-cli for the CH32H417 LA |
| [WeActStudio/CH32H417_LogicAnalyzer_Upgrade](https://github.com/WeActStudio/CH32H417_LogicAnalyzer_Upgrade) | WeAct upgrade tool (ISP flow) |
| ★ [YeziCZH/CH32H417_DFU](https://github.com/YeziCZH/CH32H417_DFU) | 16 KB CherryUSB DFU bootloader — alternative programming path |
| [VoltCyclone/Hurra-v3](https://github.com/VoltCyclone/Hurra-v3) | Dual-core USB HID relay |
| ★ [mamkincoderr/H417_Cmake](https://github.com/mamkincoderr/H417_Cmake) | Dual-core CMake + Ninja + GCC 15 template |
| [mamkincoderr/H417_FreeRTOS](https://github.com/mamkincoderr/H417_FreeRTOS) | FreeRTOS + lwIP on V5F |
| [Sergo101/cmake_ch32h417_test](https://github.com/Sergo101/cmake_ch32h417_test) | Dual-core CMake + VSCode debug |
| [no010/ch32h417-bare-metal-guide](https://github.com/no010/ch32h417-bare-metal-guide) | Bare-metal C + Rust bring-up tutorial |
| [lightzero521/h417-lzport-template](https://github.com/lightzero521/h417-lzport-template) | Dual-core bring-up template |
| [lightzero521/CH32H417-ThreadX](https://github.com/lightzero521/CH32H417-ThreadX) | ThreadX port |
| [823984418/ch32h417_demo_rs](https://github.com/823984418/ch32h417_demo_rs) | Rust demo |
| [ririyeye/ch32h417-async](https://github.com/ririyeye/ch32h417-async) / [ch32h417-blink](https://github.com/ririyeye/ch32h417-blink) | Rust async / blink |
| [dovandung/ch32h417trace](https://github.com/dovandung/ch32h417trace) | Trace tooling |

## Tools (programming / debug — not H417-specific)

| Repo | What | Relevance |
|------|------|-----------|
| ★ [ch32-rs/wchisp](https://github.com/ch32-rs/wchisp) | Rust USB/UART ISP tool | Host-side flashing via bootloader — **no CH32H41x device file yet (2026-11-12)**; would need adding |
| [ch32-rs/wlink](https://github.com/ch32-rs/wlink) | Rust WCH-Link tool | SDI protocol reference |
| [cnlohr/ch32fun](https://github.com/cnlohr/ch32fun) | Minimal open stack + minichlink | **Supports CH32H41x** (`ch32h41xhw.h`, minichlink `chips.c`) — best reference for an RP2350 SDI programmer |
| ★ [Apache02/pico-rvd](https://github.com/Apache02/pico-rvd) | RP2040 as CH32V003 flasher/debugger (PIO SWIO) | Starting point for RP2350 → CH32 SDI |
| [mean00/swindle](https://github.com/mean00/swindle) | BMP fork with CH32V RVSWD | 2-wire SDI reference |

## Listed but not cloned (applications, little design relevance)

Audio/PD/AI/robotics apps: 730KDong/ch32h417_audio, acceleraser/-CH32H417-AI-, ArmstrongSubero/(RISCV-Embedded, Rovari-SDK, rovari-studio, rvTTS),
Bradley-Lyu/CH32H417-AIoT-Ecobox, David-726/TFLM_TinyML_CH32H417, EBREAK/forth_ch32h417, gamarrasanza/SoundEffectGenerator,
Haru-Skythos/CH32_Smart_Charger, inuchanbt/ch32h417-pd-interrogator, jiangalsoflow/ch32h417eye-track-use-ml, Lan-306/-CH32H417-,
lightzero521/(CH32H417-CycloneTCP-Bringup, CommHub-CH32H417), Liren66/OmniCore-SDR-Linux, LYT-0699/*, openwch/CH32H41x_BetaFlight_Lib,
Oliveryang258/CH32H417-Drone, q7300/CH32H417-emotion-sensing, qinyunti/CH32H417-PDM-MIC, QX0826/CH32H417-EdgeGimbal,
shlllshlll/logic-view, STM32F407VET6/-CH32H417-AI-, threeye11/CH32H417-PestInspect-Mobile, Tingy-Lee/flight_control,
Tokisaki3333/*, Tom-star2004/*, TTTao163/*, wasdwasd0105/ch32h417-virtual-image, wdnmd-wdnmd6/*, XiaoN675/CH32H417-RTT-Study,
Y-star-49/CH32H417. Add any to `repos.txt` to clone.
