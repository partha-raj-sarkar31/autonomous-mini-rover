# Bill of materials (provisional)

| Item | Target | Verify before use |
|---|---|---|
| Controller | Arduino Uno R3 | Genuine/clone, 5 V logic, pinout |
| Motor driver | L293D IC/module | Exact board, continuous/peak current, voltage drop and thermal dissipation |
| Motors | 2 × DC gear motors, model TBD | Rated voltage, stall current, no-load/output RPM |
| Range sensor | TBD | Model, logic voltage, interface, minimum/maximum range |
| Battery | 3S 900 mAh, 11.1 V nominal | Chemistry, max charge voltage, discharge current, protection |
| Regulator | Buck converter TBD | 3S input range, 5 V output and sufficient current |
| Chassis/wheels | TBD | Dimensions, traction, motor mounting |
| Safety | Switch, fuse, connectors, wire | Rated for expected current |

The 3S pack is 12.6 V at full charge. Do not connect it to the Uno 5 V pin. Verify whether the chosen L293D module supports the motor supply and motor stall current. Many small L293D modules are unsuitable for high-stall-current motors.
