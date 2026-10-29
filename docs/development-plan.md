# Development plan (5–10 days after components arrive)

## Day 0–1: identify and power safely
- Record exact Uno, range sensor, L293D board/IC, motor and battery models.
- Verify motor stall current against L293D ratings and thermal limits.
- Select regulator for the Uno and sensor; measure rails before connection.

## Day 1–2: sensor validation
- Implement range adapter with explicit timeout and invalid-reading flag.
- Record readings at known distances; compare to ruler; identify minimum reliable range.
- Test disconnected sensor, timeout and out-of-range cases.

## Day 2–3: motor validation
- Lift wheels; verify direction and stop behavior at low PWM.
- Confirm no unexpected movement at reset and on invalid sensor input.

## Day 3–5: integrate state machine
- Integrate non-blocking state updates with `millis()`.
- Verify threshold boundary, turn timeout, recheck, fault latch and reset policy.
- Begin with low speed and a soft obstacle in a clear test area.

## Day 5–7: controlled obstacle trials
- Measure stopping distance from defined speeds and approach distances.
- Test varied obstacle distance, surface and battery condition.
- Count successful avoidance, collisions/contact, missed detections and false positives.

## Day 7–10: refine and report
- Adjust threshold/timeout one at a time; publish trial CSV and firmware revision.
- Consider a servo-mounted sensor or additional sensing if choosing turn direction is required.
- Record limitations; never claim collision avoidance from timed-turn logic alone.
