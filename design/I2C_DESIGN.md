# I2C Bus Design Notes

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-13  
**Version:** 1.0  

---

## Overview

The I2C bus connects environmental sensors to the Raspberry Pi 2, which is dedicated to environmental sensor management. The bus runs between two enclosures — the main compute enclosure and the remote sensor enclosure housing the Discovery Dish rotator and field sensors.

The I2C bus also serves sensors inside the main enclosure, specifically the BME280 located inside the SDR junction box for thermal monitoring.

---

## I2C Fundamentals

### Protocol
- Two wire serial bus: SDA (data) and SCL (clock)
- Maximum bus capacitance: 400 pF (I2C specification)
- Pull-up resistors required on both SDA and SCL
- Multiple devices share the bus — each has a unique 7-bit address

### Speed Modes
| Mode | Speed | Notes |
|------|-------|-------|
| Standard | 100 kHz | Most forgiving, recommended for long runs |
| Fast | 400 kHz | Qwiic standard — verify with actual cable capacitance |
| Fast-mode Plus | 1 MHz | Not recommended for inter-enclosure runs |

**Recommended: Standard mode (100 kHz) for inter-enclosure run given cable length and number of devices.**

---

## Physical Bus Architecture

### Inter-Enclosure Cable
- **Cable:** Belden 8102 or equivalent low-capacitance shielded twisted pair
  - 24 AWG (7/0.2 metric equivalent)
  - Capacitance: ~12.5 pF/ft (Belden 8102)
  - Dual shielded: Beldfoil + tinned copper braid
  - 300V rated
- **Length:** ~5ft (1.5m) between enclosures
- **Capacitance budget used:** ~62 pF at 5ft — well within 400 pF limit

### Pair Assignment
| Pair | Signals | Notes |
|------|---------|-------|
| Pair 1 | SDA + GND | Signal on one conductor, ground reference on other |
| Pair 2 | SCL + GND | Signal on one conductor, ground reference on other |
| Pair 3 | VCC + GND | 3.3V power if powering remote sensors from Pi side |
| Pair 4 | Spare | Reserved for future use |

### Shield Termination
- Shield connected to GND at **Pi end only**
- Far end (sensor enclosure) left floating
- Prevents ground loops while maintaining noise rejection
- Single-end grounding standard practice for short inter-enclosure runs

---

## Voltage Levels

- Raspberry Pi I2C: **3.3V logic** — GPIO pins are NOT 5V tolerant
- BME280: 3.3V native
- Qwiic standard: 3.3V / 400 kHz
- All devices on this bus must be 3.3V compatible — verify before connecting

---

## Devices on Bus

### Inside Main Enclosure

**BME280 — SDR Junction Box**
- Purpose: SDR thermal monitoring
- Measures: temperature, humidity, barometric pressure
- I2C address: 0x76 (SDO to GND) or 0x77 (SDO to VCC)
- Location: inside steel junction box housing Airspy R2 and RTL-SDR V4c
- Cable exits junction box through copper foil wrapped egress point — see RF_DESIGN.md

### Remote Sensor Enclosure (at Discovery Dish)

**BME280 — Field Environmental**
- Purpose: ambient environmental monitoring at dish location
- Measures: temperature, humidity, barometric pressure
- I2C address: must differ from junction box BME280 — set via SDO pin
- Relevant for: atmospheric correction, observation logging, dew point monitoring

**IMU — Dish Orientation**
- Purpose: dish pointing verification and orientation tracking
- Connected via Qwiic daisy chain from BME280
- Specific device TBD — verify I2C address compatibility with other bus devices

### Address Map
| Device | Location | Address | SDO Setting |
|--------|----------|---------|-------------|
| BME280 #1 | Junction box | 0x76 | SDO to GND |
| BME280 #2 | Remote enclosure | 0x77 | SDO to VCC |
| IMU | Remote enclosure | TBD | TBD |

**Verify no address conflicts before connecting all devices.**

---

## Pull-up Resistors

### Requirements
- Both SDA and SCL require pull-up resistors to 3.3V
- Value determines rise time — must suit bus capacitance and speed

### Calculation
For Standard mode (100 kHz) with ~200 pF total bus capacitance (cable + devices):
- Minimum pull-up: ~1 kΩ (maximum sink current limited by device specs)
- Maximum pull-up: ~10 kΩ (rise time limit)
- **Recommended: 4.7 kΩ** — standard value, well within spec at 100 kHz

### Qwiic Boards
Qwiic devices often have onboard pull-up resistors (typically 4.7 kΩ). Multiple Qwiic devices on the same bus stack pull-ups in parallel, reducing effective resistance:
- 1 device with 4.7 kΩ: 4.7 kΩ effective
- 2 devices with 4.7 kΩ: 2.35 kΩ effective
- 3 devices with 4.7 kΩ: 1.57 kΩ effective

Lower effective resistance increases bus current and reduces rise time — generally acceptable at 100 kHz but monitor if adding many Qwiic devices.

**If pull-ups stack too low, disable onboard pull-ups on some Qwiic boards (check for pull-up disable solder jumper).**

### Raspberry Pi Internal Pull-ups
Pi GPIO I2C pins have weak internal pull-ups (~50 kΩ) — insufficient alone for this bus. External pull-ups required.

---

## Cable Capacitance Budget

| Source | Capacitance |
|--------|-------------|
| Belden 8102, 5ft | ~62 pF |
| BME280 #1 (junction box) | ~5-10 pF |
| BME280 #2 (remote) | ~5-10 pF |
| IMU (TBD) | ~5-10 pF |
| PCB traces and connectors | ~10-20 pF |
| **Estimated total** | **~90-110 pF** |
| **I2C specification limit** | **400 pF** |

Comfortable margin at Standard mode. Fast mode (400 kHz) also viable with this capacitance budget.

---

## Connector Strategy

### Inter-Enclosure Connection
- Belden 8102 or equivalent terminated at both ends
- No proprietary connectors — screw terminals or soldered connections preferred for reliability
- Weatherproof entry at remote enclosure via cable gland
- See ENCLOSURE_DESIGN.md for mechanical details

### Qwiic Connections (remote enclosure)
- Standard Qwiic JST connector daisy chain
- BME280 → IMU chain
- Qwiic cables rated for 3.3V, 400 kHz — compatible with our 100 kHz operation
- Keep Qwiic cable lengths short inside remote enclosure

---

## EMI Considerations

### Shielded Cable Importance
The I2C inter-enclosure cable runs alongside the PoE Cat6 cable in the PVC conduit. Cat6 carries:
- 24V PoE power (Tycon POE-SPLT-BT-UNI-P set to 24V)
- Ethernet data

Potential for interference from PoE switching transients onto I2C bus. Shielded twisted pair cable mitigates this. Single-end shield grounding prevents ground loops.

### Inside Main Enclosure
- I2C cable exits junction box through copper foil wrapped egress — see RF_DESIGN.md
- Route I2C cable away from Pi 5 and its USB cables where possible
- Pi 5 is a significant broadband noise source — physical separation preferred

### Ferrite Chokes
- Not typically required on I2C at these lengths and speeds
- If noise observed on bus: Type 31 ferrite, single turn, at Pi end
- BME280 inside junction box inherits junction box RF shielding — well protected

---

## Software Notes

### Pi 2 Role
Pi 2 is dedicated to environmental sensor management:
- Polls BME280 #1 (junction box) — SDR thermal monitoring
- Polls BME280 #2 (remote) — field environmental monitoring
- Reads IMU — dish orientation data
- Logs all data with timestamps
- Exposes data to Pi 5 via local network for science pipeline integration
- Triggers alerts if thermal thresholds exceeded — see HEAT_DESIGN.md

### Recommended Libraries
- **smbus2** — Python I2C library, well maintained
- **RPi.bme280** — BME280 specific library
- **adafruit-circuitpython-bme280** — Adafruit alternative, good documentation

### Bus Scanning
Before first use, scan the I2C bus to verify all devices present and no address conflicts:

```bash
sudo i2cdetect -y 1
```

Expected output should show device addresses at expected locations. Document the scan result as baseline.

### Enabling I2C on Raspberry Pi
```bash
sudo raspi-config
# Interface Options → I2C → Enable
```

Or add to /boot/config.txt:
```
dtparam=i2c_arm=on
```

### Example BME280 Read (Python)
```python
import smbus2
import bme280

port = 1
address = 0x76  # Junction box BME280
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)

print(f"Temperature: {data.temperature:.2f}°C")
print(f"Humidity: {data.humidity:.2f}%")
print(f"Pressure: {data.pressure:.2f} hPa")
print(f"Dew point: {dewpoint(data.temperature, data.humidity):.2f}°C")
```

### Dew Point Calculation
```python
import math

def dewpoint(temperature_c, humidity_percent):
    """Magnus formula dew point approximation"""
    a = 17.625
    b = 243.04
    alpha = (a * temperature_c / (b + temperature_c)) + math.log(humidity_percent / 100.0)
    return (b * alpha) / (a - alpha)
```

---

## Installation Notes

### Cable Routing
1. I2C cable runs inside main enclosure alongside USB cables
2. Exits main enclosure through same cable gland route as Cat6 (or dedicated gland)
3. Runs through PVC conduit with Cat6 to remote enclosure
4. Enters remote enclosure through cable gland
5. Terminates at BME280 and IMU inside remote enclosure

### Assembly Sequence
1. Install BME280 #1 inside junction box before closing
2. Route I2C cable through copper foil wrapped egress hole
3. Connect to Pi 2 via screw terminals or soldered connection
4. Route inter-enclosure cable through conduit
5. Terminate at remote enclosure sensors
6. Scan bus, verify all devices, document addresses
7. Run test data collection before field deployment

---

## Open Questions / Future Work

- [ ] Confirm IMU device selection and I2C address
- [ ] Verify Qwiic pull-up resistor situation on chosen BME280 breakout boards
- [ ] Decide on BME280 breakout board — SparkFun Qwiic vs Adafruit vs bare module
- [ ] Determine whether Pi 2 I2C speed should be 100 kHz or 400 kHz — bench test with actual cable
- [ ] Design data logging schema for environmental data
- [ ] Define alert thresholds and alert mechanism (local log, network message to Pi 5)
- [ ] Consider adding second IMU inside main enclosure for enclosure orientation reference
- [ ] Evaluate I2C bus extender (e.g. PCA9615) if longer runs needed in future

---

## Related Documents
- RF_DESIGN.md — junction box design, cable egress shielding
- HEAT_DESIGN.md — thermal monitoring thresholds, BME280 placement rationale
- SENSOR_DESIGN.md — full sensor architecture and data pipeline
- POWER_DESIGN.md — 3.3V power distribution to sensors
- ENCLOSURE_DESIGN.md — mechanical design, cable glands, conduit routing

---

*Document status: Initial design notes — pre-build*
*Last updated: May 2026*
