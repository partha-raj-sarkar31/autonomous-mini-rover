#pragma once
#include <stdint.h>

namespace rover {
enum State : uint8_t { IDLE, FORWARD, STOP, TURN, RECHECK, FAULT };
enum Motion : uint8_t { MOTOR_STOP, MOTOR_FORWARD, MOTOR_TURN_LEFT, MOTOR_TURN_RIGHT };

struct Config {
    float obstacle_cm = 20.0f;
    uint32_t turn_timeout_ms = 450;
    uint32_t recheck_timeout_ms = 250;
    uint8_t invalid_limit = 3;
};
struct Input {
    bool start;
    bool distance_valid;
    float distance_cm;
    uint32_t now_ms;
};
struct Output { State state; Motion motion; bool fault; };

class Navigator {
public:
    explicit Navigator(const Config& cfg = Config())
        : cfg_(cfg), state_(IDLE), entered_ms_(0), invalid_count_(0) {}

    Output update(const Input& in) {
        if (state_ == FAULT) return output(MOTOR_STOP, true);
        if (!in.distance_valid || in.distance_cm < 0.0f) {
            if (invalid_count_ < 255) ++invalid_count_;
            if (invalid_count_ >= cfg_.invalid_limit) {
                state_ = FAULT;
                return output(MOTOR_STOP, true);
            }
            state_ = STOP;
            entered_ms_ = in.now_ms;
            return output(MOTOR_STOP, false);
        }
        invalid_count_ = 0;

        switch (state_) {
        case IDLE:
            if (in.start) { state_ = FORWARD; entered_ms_ = in.now_ms; }
            return output(MOTOR_STOP, false);
        case FORWARD:
            if (in.distance_cm <= cfg_.obstacle_cm) {
                state_ = STOP; entered_ms_ = in.now_ms;
                return output(MOTOR_STOP, false);
            }
            return output(MOTOR_FORWARD, false);
        case STOP:
            state_ = TURN; entered_ms_ = in.now_ms;
            return output(MOTOR_STOP, false);
        case TURN:
            if ((uint32_t)(in.now_ms - entered_ms_) >= cfg_.turn_timeout_ms) {
                state_ = RECHECK; entered_ms_ = in.now_ms;
                return output(MOTOR_STOP, false);
            }
            return output(MOTOR_TURN_RIGHT, false);
        case RECHECK:
            if (in.distance_cm > cfg_.obstacle_cm) {
                state_ = FORWARD; entered_ms_ = in.now_ms;
                return output(MOTOR_STOP, false);
            }
            if ((uint32_t)(in.now_ms - entered_ms_) >= cfg_.recheck_timeout_ms) {
                state_ = FAULT;
                return output(MOTOR_STOP, true);
            }
            return output(MOTOR_STOP, false);
        case FAULT:
        default:
            state_ = FAULT;
            return output(MOTOR_STOP, true);
        }
    }

    State state() const { return state_; }
private:
    Config cfg_;
    State state_;
    uint32_t entered_ms_;
    uint8_t invalid_count_;
    Output output(Motion motion, bool fault) const { return {state_, motion, fault}; }
};
} // namespace rover
