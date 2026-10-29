from rover_model import Navigator

nav = Navigator()
events = [
    (True, 100.0, 0),
    (False, 100.0, 10),
    (False, 15.0, 20),
    (False, 15.0, 30),
    (False, 15.0, 500),
    (False, 35.0, 510),
]
print("Synthetic range readings (cm); software-only state-machine demo")
for start, distance, now in events:
    state, motion = nav.update(start, distance, now)
    print(f"t={now:>3} ms distance={distance:>5.1f} cm -> state={state.name:<7} motion={motion}")
print("NOTE: timed turn is heuristic; this is not a hardware avoidance test.")
