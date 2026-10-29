# Wiring and electrical safety

- Battery -> fuse/switch -> motor supply input only if the driver/module supports full 3S voltage (12.6 V maximum).
- Battery -> rated buck converter -> Uno supply input through an appropriate supported path; verify 5 V rail before connecting peripherals. Never apply raw pack voltage to 5 V.
- Connect grounds appropriately between Uno, sensor, driver and regulator.
- Motor supply and logic supply may be separate rails; do not confuse L293D logic Vcc1 and motor Vcc2.
- Check motor stall current against the L293D's package/module rating and thermal limits; voltage drop can cause heating and weak motors.
- Range sensor echo/output voltage must be compatible with Uno inputs.
- Add a physical power switch; disconnect battery before changing wiring.
- Initial motor-direction tests must be performed with wheels raised.
