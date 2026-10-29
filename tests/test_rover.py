import unittest
from rover_model import Navigator, Config, State

class RoverTests(unittest.TestCase):
    def start_forward(self, nav):
        nav.update(True, 100, 0)
        return nav.update(False, 100, 1)

    def test_idle_then_forward(self):
        nav = Navigator()
        self.assertEqual(nav.update(False, 100, 0)[0], State.IDLE)
        self.assertEqual(self.start_forward(nav), (State.FORWARD, "FORWARD"))

    def test_threshold_boundary_stops(self):
        nav = Navigator()
        self.start_forward(nav)
        self.assertEqual(nav.update(False, 20.0, 10), (State.STOP, "STOP"))

    def test_clear_distance_keeps_forward(self):
        nav = Navigator()
        self.start_forward(nav)
        self.assertEqual(nav.update(False, 20.1, 10), (State.FORWARD, "FORWARD"))

    def test_invalid_reading_stops_then_faults_after_limit(self):
        nav = Navigator(Config(invalid_limit=2))
        self.start_forward(nav)
        self.assertEqual(nav.update(False, None, 10), (State.STOP, "STOP"))
        self.assertEqual(nav.update(False, -1, 20), (State.FAULT, "STOP"))
        self.assertEqual(nav.update(False, 100, 30), (State.FAULT, "STOP"))

    def test_turn_timeout_then_recheck(self):
        nav = Navigator(Config(turn_timeout_ms=50))
        self.start_forward(nav)
        nav.update(False, 10, 10)   # STOP
        nav.update(False, 10, 11)   # enter TURN
        self.assertEqual(nav.update(False, 10, 61), (State.RECHECK, "STOP"))

    def test_recheck_clear_returns_to_forward(self):
        nav = Navigator()
        self.start_forward(nav)
        nav.update(False, 10, 10)
        nav.update(False, 10, 11)
        nav.update(False, 10, 500) # timeout -> RECHECK
        self.assertEqual(nav.update(False, 30, 510), (State.FORWARD, "STOP"))

    def test_recheck_timeout_faults(self):
        nav = Navigator(Config(turn_timeout_ms=5, recheck_timeout_ms=5))
        self.start_forward(nav)
        nav.update(False, 10, 10)
        nav.update(False, 10, 11)
        nav.update(False, 10, 16)  # RECHECK
        self.assertEqual(nav.update(False, 10, 21), (State.FAULT, "STOP"))

if __name__ == "__main__":
    unittest.main()
