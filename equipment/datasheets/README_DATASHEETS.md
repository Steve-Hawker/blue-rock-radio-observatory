# Equipment Datasheets

Component datasheets and product documentation for all Blue Rock
Radio Observatory hardware.

---

## Contents

| File | Component | Key specs | Date added |
|---|---|---|---|
| QPL9547_Data_Sheet.pdf | Qorvo QPL9547 LNA1 | NF 0.17dB @ 1420MHz · Gain 19.5dB · OIP3 +39dBm | 2026-05-04 |
| RTLSDR_V4_Datasheet_V_1_0.pdf | RTL-SDR Blog V4/V4c | 8-bit · 1PPM TCXO · triplexer · 28-43dB OOB isolation | 2026-05-04 |
| Discovery_Dish_CrowdSupply.pdf | Discovery Dish + HI Feed | 70cm · 17.7dBi gain · 20-22° beamwidth · LMR240 cable | 2026-05-04 |
| RTL-SDR_Dipole_Set_eBay.pdf | RTL-SDR Blog dipole set | Short arms to 13cm · Long arms to 100cm · SMA | 2026-05-04 |
| ADF4351_board_eBay.pdf | ADF4351 signal source | 35M-4.4GHz · ±50ppm · SPI control · 5V USB | 2026-05-04 |
| SMA_attenuator_30dB_eBay.pdf | Gwave SMA attenuator 30dB | DC-8GHz · brass body · SMA M-F | 2026-05-04 |
| RTL-SDR_Blog_V3_Dongles_User_Guide.pdf | RTL-SDR Blog V3 user guide | Bias tee · direct sampling · clock sharing | 2026-05-04 |
| RTL-SDR_Blog_V4_Users_Guide.pdf | RTL-SDR Blog V4 user guide | Driver install · MacOS GQRX · bias tee · EEPROM | 2026-05-04 |
| Using_our_new_Dipole_Antenna_Kit.pdf | RTL-SDR dipole kit guide | Arm lengths · 2cm internal metal · M5 thread · mounting | 2026-05-04 |
| Phihong_POE48-120BT-R.pdf | Phihong PoE splitter 48W | 12V@4A output · **MAX +40°C — disqualified for outdoor use** | 2026-05-04 |
| Tycon_POE-SPLT-BT-UNI-P.pdf | Tycon PoE splitter 90W | 5V@14A + 12V@5.9A · -40°C to +75°C · DIN mount · **selected** | 2026-05-04 |
| TP-Link_TL-POE170S.pdf | TP-Link PoE injector 60W | 802.3bt · 60W max · 0°C to 45°C · indoor use · **selected** | 2026-05-04 |
| QILIPSU_Enclosure_350x250x150.pdf | QILIPSU IP65 stainless enclosure | 304 SS · 350×250×150mm · IP65 · DIN plate · lockable · $89.99 · **selected over KrakenRF DDOEE** | 2026-05-04 |

---

## Key Values for INV001 Noise Budget

Extracted from datasheets for use in Friis cascade calculation:

### QPL9547 LNA1 — at 1420 MHz (interpolated from datasheet)

| Parameter | Value | Source |
|---|---|---|
| NFmin | ~0.17 dB | Noise parameters table, interpolated 1.4–1.6 GHz |
| Gain (S21) | ~21.5 dB | S-parameters table, interpolated 1.3–1.5 GHz |
| Output P1dB | ~+22 dBm | Performance plots |
| OIP3 | ~+38.5 dBm | Performance plots |
| Supply | 5V, 65 mA | Electrical specifications |

Note: Datasheet test conditions are at 1900 MHz. Values at 1420 MHz
interpolated from S-parameter and noise parameter tables. INV001
should use the interpolated 1420 MHz values, not the headline 1900 MHz
specifications.

### RTL-SDR V4c — at 1420 MHz

| Parameter | Value | Source |
|---|---|---|
| ADC bits | 8 | Datasheet |
| LO stability | 1 PPM TCXO | Datasheet |
| Bias tee | 4.5V, 180mA | Datasheet |
| OOB isolation improvement vs V3 | 28–43 dB at 1420 MHz | Two-tone test |
| Frequency range | 500 kHz – 1.766 GHz | Datasheet |

### Discovery Dish — at 1420 MHz

| Parameter | Value | Source |
|---|---|---|
| Dish diameter | 70 cm | Product page |
| Simulated gain | 17.7 dBi | Gain/return loss plots |
| Beamwidth (3dB) | ~20–22° | Angular width from simulation |
| Sidelobe level | -19 dB (Phi=0), -15.1 dB (Phi=90) | Simulation |
| Cable included | 6m LMR240-equivalent | Product description |

Note: Beamwidth from simulation is 20–22°, slightly wider than the
17° estimate used in BEAM_AND_RESOLUTION.md. Update that document
with the measured value from commissioning Cas A beam scan.

---

## Power Budget

| Component | Voltage | Est. current | Est. power |
|---|---|---|---|
| Raspberry Pi 5 | 5V | ~2.5A | ~12.5W |
| Airspy R2 | 5V | ~0.5A | ~2.5W |
| RTL-SDR V4c | 5V | ~0.27A | ~1.4W |
| ADF4351 board | 5V | ~0.5A | ~2.5W |
| Discovery Drive | 12V | ~1A typical | ~12W |
| **Total load** | | | **~31W** |
| TL-POE170S output | — | — | 60W max |
| Tycon splitter efficiency | — | — | 80% min |
| **Available at load** | | | **~48W** |
| **Headroom** | | | **~17W** |

Comfortable margin. Discovery Drive current draw under slewing load to be
confirmed — if significantly above 1A, revisit budget.

---

- [x] Update BEAM_AND_RESOLUTION.md — beamwidth 17° → 20-22° (from simulation) — done v1.1
- [x] Update BEAM_AND_RESOLUTION.md — cable is LMR240-equivalent not LMR200 — done v1.1
- [x] Update DIPOLE_ANTENNA_DESIGN.md — stock arms cannot reach 1420 MHz resonant length; custom brass elements required — done v2.0
- [ ] Complete INV001 with QPL9547 interpolated values at 1420 MHz
- [ ] Note V4c triplexer improvement in SDR_SELECTION.md and RFI_OVERVIEW.md
- [ ] Add GQRX MacOS bias tee device string to RASPBERRY_PI_SETUP.md: rtl=0,bias=1
- [ ] Create design/POWER_ARCHITECTURE.md — TL-POE170S + Tycon POE-SPLT-BT-UNI-P + Pi 5 architecture (pending Murata DC-DC confirmation, now eliminated by Tycon unit)
