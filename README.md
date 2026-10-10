# Autonomous Mini Rover

A small STM32-controlled mobile robot designed to detect obstacles and
perform basic autonomous movement using sensor feedback.

> **Project status:** In development\
> **Performance status:** Baseline testing pending. Obstacle-avoidance
> and safety performance have not yet been validated.

## Demo

**Prototype video:** *Placeholder --- add a link after recording a real
hardware demonstration.*

`[Add demo video URL here]`

## Objectives

-   Control a differential-drive robot using two independently driven
    motors.
-   Measure distance with an ultrasonic sensor or another documented
    range sensor.
-   Implement obstacle detection, stop/turn behavior, and a simple
    navigation state machine.
-   Evaluate detection performance, stopping distance, and
    obstacle-avoidance success.
-   Keep hardware assumptions and test conditions documented.

## Hardware

Replace placeholders with the actual components used.

-   Development board: **\[exact board/model to be added\]**
-   Motor driver: **\[model to be added\]**
-   Motors, wheels, and chassis: **\[specifications to be added\]**
-   Range sensor: **\[model to be added\]**
-   Battery, regulator, and power switch: **\[specifications to be
    added\]**
-   Optional wheel encoders: **\[model/status to be added\]**

See [`hardware/`](hardware/) for the BOM, circuit diagram, pin map, and
chassis documentation.

## Repository Structure

``` text
autonomous-mini-rover/
├── firmware/       # Motor control, sensor driver, navigation state machine
├── hardware/       # Circuit, pin map, BOM, chassis files
├── tests/          # Obstacle trials, stopping-distance data, success-rate logs
├── docs/           # State machine, setup guide, test reports
├── README.md
├── LICENSE
└── .gitignore
```

## Software and Setup

1.  Install the development toolchain appropriate for the selected STM32
    board.
2.  Confirm GPIO, PWM, timer/input-capture, and ADC requirements for the
    selected hardware.
3.  Wire the motor driver and range sensor according to their datasheets
    and the verified board pinout.
4.  Check all signal voltage levels before connecting sensor outputs to
    the MCU.
5.  Test sensor readings with the motors disconnected or disabled.
6.  Test each motor at low PWM while the wheels are lifted.
7.  Run the navigation state machine in a clear, controlled area.

**Important:** Some ultrasonic modules use a 5 V ECHO signal. Verify the
module's electrical specification and use level shifting where required
for a 3.3 V STM32 input.

## Initial Navigation Logic

The first version may use a simple state machine:

-   `IDLE`: motors stopped until start conditions are met.
-   `FORWARD`: move while the measured distance is above the configured
    threshold.
-   `STOP`: stop when an obstacle is detected inside the threshold.
-   `TURN`: rotate or steer for a configured interval.
-   `RECHECK`: measure again and decide whether to continue or repeat
    avoidance.
-   `FAULT`: stop motors when sensor readings are invalid or a fault is
    detected.

Document thresholds, timeouts, sensor update rate, and failure behavior
in `docs/`. A timed turn is a starting point, not a guarantee of
collision-free navigation.

## Testing and Metrics

Test in a controlled environment with clearly defined obstacle positions
and approach speeds.

  -----------------------------------------------------------------------
  Metric                  Definition              Status
  ----------------------- ----------------------- -----------------------
  Obstacle-detection      Correct detections      Pending testing
  performance             against labeled test    
                          cases                   

  Stopping distance       Distance traveled from  Pending testing
                          the defined detection   
                          point to rest           

  Avoidance success rate  Successful avoidance    Pending testing
                          trials / total valid    
                          trials                  

  False-positive rate     Obstacle detections     Pending testing
                          when no obstacle is     
                          present                 

  Sensor failure behavior Whether invalid         Pending testing
                          readings lead to a safe 
                          stop                    
  -----------------------------------------------------------------------

For every test, record obstacle type/size, distance, approach speed,
floor surface, battery condition, and firmware revision.

## Baseline Results

**Status: Pending testing.** No obstacle-detection accuracy,
stopping-distance, or avoidance-success figures are available yet.

Once trials are completed, report the number of trials, test setup,
metric definitions, raw data location, summary statistics, and known
limitations. Do not describe the rover as safe for public-road or
human-critical use.

## Safety

-   Test at low speed in a clear, controlled area.
-   Keep hands and loose objects away from wheels and gears.
-   Use a hardware power switch that can quickly cut motor power.
-   Do not rely on a low-cost ultrasonic sensor as the sole safety
    system around people or vehicles.
-   Verify battery protection, polarity, and motor-driver current
    limits.

## Roadmap

-   [ ] Confirm board and component models
-   [ ] Add circuit, pin map, and BOM
-   [ ] Validate range-sensor readings
-   [ ] Validate low-speed motor control
-   [ ] Implement navigation state machine
-   [ ] Define repeatable obstacle test cases
-   [ ] Record baseline results
-   [ ] Add real prototype demo video

## License

The project license has not yet been selected. Add the chosen license
text to `LICENSE` before describing this repository as open source.
