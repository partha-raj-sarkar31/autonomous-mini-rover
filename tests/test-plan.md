# Test plan

## Software-only
Run `python -m unittest discover -s tests -v` and `python tests/demo.py`. Unit tests cover IDLE/FORWARD, threshold boundary, clear distance, invalid samples, fault latch, turn timeout and recheck behavior.

## Hardware protocol (pending)
1. Record firmware revision, sensor model, test surface, battery voltage, motor details and obstacle type.
2. Validate sensor readings at measured distances; record invalid/timeouts separately.
3. With wheels raised, test forward, left/right turn, stop, reset and power-loss behavior.
4. In a clear area, approach a soft obstacle at low speed; use a spotter and physical power switch.
5. Record approach speed or test condition, initial distance, stopping distance, detection result, turn direction, contact/collision, outcome, false positive and battery voltage.
6. Detection rate = detected obstacle trials / obstacle trials; avoidance success = no-contact successful trials / obstacle trials. State sample count and conditions.
7. Results remain Pending hardware validation until actual trials are recorded. Do not interpret software test pass as physical collision avoidance.
