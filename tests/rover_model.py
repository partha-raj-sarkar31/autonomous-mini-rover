"""Hardware-independent reference navigation model for deterministic tests."""
from dataclasses import dataclass
from enum import Enum, auto

class State(Enum):
    IDLE = auto()
    FORWARD = auto()
    STOP = auto()
    TURN = auto()
    RECHECK = auto()
    FAULT = auto()

@dataclass
class Config:
    obstacle_cm: float = 20.0
    turn_timeout_ms: int = 450
    recheck_timeout_ms: int = 250
    invalid_limit: int = 3

class Navigator:
    def __init__(self, config=None):
        self.cfg = config or Config()
        self.state = State.IDLE
        self.entered = 0
        self.invalid_count = 0

    def update(self, start, distance_cm, now_ms):
        if self.state is State.FAULT:
            return self.state, "STOP"
        if distance_cm is None or distance_cm < 0:
            self.invalid_count += 1
            if self.invalid_count >= self.cfg.invalid_limit:
                self.state = State.FAULT
                return self.state, "STOP"
            self.state, self.entered = State.STOP, now_ms
            return self.state, "STOP"
        self.invalid_count = 0
        if self.state is State.IDLE:
            if start:
                self.state, self.entered = State.FORWARD, now_ms
            return self.state, "STOP"
        if self.state is State.FORWARD:
            if distance_cm <= self.cfg.obstacle_cm:
                self.state, self.entered = State.STOP, now_ms
                return self.state, "STOP"
            return self.state, "FORWARD"
        if self.state is State.STOP:
            self.state, self.entered = State.TURN, now_ms
            return self.state, "STOP"
        if self.state is State.TURN:
            if now_ms - self.entered >= self.cfg.turn_timeout_ms:
                self.state, self.entered = State.RECHECK, now_ms
                return self.state, "STOP"
            return self.state, "TURN_RIGHT"
        if self.state is State.RECHECK:
            if distance_cm > self.cfg.obstacle_cm:
                self.state, self.entered = State.FORWARD, now_ms
                return self.state, "STOP"
            if now_ms - self.entered >= self.cfg.recheck_timeout_ms:
                self.state = State.FAULT
                return self.state, "STOP"
            return self.state, "STOP"
        self.state = State.FAULT
        return self.state, "STOP"
