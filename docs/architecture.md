# Architecture and requirements

## Data flow
Range sensor adapter -> validated sample (distance plus validity/timeout) -> `Navigator.update()` -> motion request -> motor adapter -> L293D.

## State machine
- `IDLE`: motors stopped until start command.
- `FORWARD`: advance while valid distance is strictly greater than obstacle threshold.
- `STOP`: issue stop before a turn.
- `TURN`: request a timed right turn for a bounded interval.
- `RECHECK`: stop and evaluate a new reading; resume forward only if clear.
- `FAULT`: latched safe-stop state after repeated invalid readings or a failed recheck.

The direction is a provisional heuristic, not an assertion that the right side is clear. There is no left/right scan in the current design. Invalid samples stop motion immediately; repeated invalid readings latch FAULT. Arduino integration must use non-blocking `millis()` timing and must ensure the motor adapter always maps STOP to both motors disabled/braked as supported by the module.

## Hardware requirements
Confirm range sensor model and voltage/interface; motor rated voltage and stall current; exact L293D IC/module and thermal arrangement; battery chemistry/rating; regulator; chassis and wheel dimensions. No physical compatibility or avoidance performance is verified yet.
