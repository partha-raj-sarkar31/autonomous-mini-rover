# Autonomous Mini Rover 

**Robotics Society of Varendra University (RSVU), Bangladesh**  
**Status:** software prototype / hardware integration pending

A small differential-drive rover software foundation targeting Arduino Uno R3, an L293D motor driver, DC motors, a range sensor (exact model TBD), and a proposed 3S 900 mAh, 11.1 V battery pack. This repository currently demonstrates navigation logic in software; it does not prove physical obstacle avoidance.

## Objectives
- Separate range sensing, motor commands, and navigation decisions.
- Implement `IDLE`, `FORWARD`, `STOP`, `TURN`, `RECHECK`, and `FAULT` states.
- Treat invalid distance readings and timeouts as explicit conditions.
- Provide deterministic tests and a synthetic demonstration before hardware integration.

## Features
- Portable C++ navigation state machine in `firmware/`.
- Python reference model, unit tests, and software-only demo in `tests/`.
- Provisional BOM, pin map, wiring and electrical checklist.
- Staged hardware test protocol.
## Repository Structure

``` text
autonomous-mini-rover/
├── README.md
├── .gitignore
├── CONTRIBUTING.md
├── firmware/
│   ├── rover_navigation.h
│   └── smoke.cpp
├── hardware/
│   ├── BOM.md
│   ├── pin-map.md
│   └── wiring.md
├── docs/
│   ├── architecture.md
│   └── development-plan.md
└── tests/
    ├── rover_model.py
    ├── test_rover.py
    ├── demo.py
    ├── test-plan.md
    └── example-results.csv
```

## Architecture
`range sensor adapter -> validated distance sample -> navigation state machine -> bounded motor request -> L293D adapter`

The C++ code is intended for Arduino IDE integration, but is kept independent of Arduino headers so the state machine can be compiled/tested separately. Add the sensor and motor driver adapters after confirming the actual range sensor, motor ratings, and wiring.

## Components
| Component | Target | Verification needed |
|---|---|---|
| Controller | Arduino Uno R3 / ATmega328P | Board revision/clone |
| Motor driver | L293D IC/module | Exact package/module, current and thermal limits |
| Motors | DC gear motors, model TBD | Rated voltage, stall current, gearbox/output speed |
| Range sensor | TBD (e.g. ultrasonic only if selected) | Model, voltage, interface, valid range, timeout behavior |
| Battery | 3S 900 mAh, 11.1 V nominal | Chemistry, discharge rating, protection |
| Regulator | Buck converter TBD | Input/output range and current rating |
| Chassis, wheels, switch, fuse | TBD | Mechanical and current ratings |

## Setup
Python 3.9+ is sufficient for software tests and demo; no third-party Python packages are required.

```bash
python -m unittest discover -s tests -v
python tests/demo.py
```

Portable C++ smoke compile if `g++` is available:
```bash
g++ -std=c++11 -Wall -Wextra -Werror -Ifirmware firmware/smoke.cpp -o /tmp/rover_smoke
/tmp/rover_smoke
```

For Arduino IDE integration, create/open an `.ino` sketch and include the state-machine header. Sensor and motor adapters are deliberately not wired to pins until the actual sensor and motor specifications are confirmed.

## Usage and demo
The demo uses synthetic distance readings. It demonstrates software state transitions, not real sensor measurements or collision avoidance. A timed turn is only a heuristic; it cannot guarantee that the path is clear.

## Testing
Python tests cover state transitions, threshold boundaries, invalid readings, turn timeout, and fault-stop behavior. C++ smoke compile checks the portable state-machine header. Physical stopping distance, detection accuracy, and avoidance success remain pending hardware validation.

## Results
| Evidence | Status |
|---|---|
| Python unit tests | Run locally before presentation; report actual result |
| C++ smoke compile | Run locally if compiler available |
| Arduino IDE build/upload | Pending adapter integration |
| Obstacle detection/stopping distance | Pending hardware validation |
| Avoidance success/false-positive rate | Pending hardware validation |

## Limitations
- Range sensor type and motor ratings are not yet confirmed.
- A single forward-facing sensor cannot reliably identify a safe turn direction.
- Timed turns are open-loop and can fail due to battery voltage, floor friction, motor variation, or obstacles.
- No measured detection accuracy, stopping distance, or collision-avoidance guarantee is claimed.

## Roadmap
1. Confirm sensor model and motor stall current.
2. Verify battery/regulator and L293D compatibility.
3. Integrate sensor adapter with timeout and invalid-reading handling.
4. Test motor directions with wheels raised.
5. Measure stopping distance at low speed.
6. Test obstacles with a soft barrier and safety spotter.
7. Publish raw trial data and limitations.

## Safety
Test at low speed in a clear area with a physical power switch and raised wheels for initial motor tests. Keep hands clear of drive wheels. Disconnect battery before wiring. Never feed raw 3S voltage into the Uno 5 V pin. Confirm the L293D current/thermal limits against motor stall current before use.

## License
See `LICENSE`.

