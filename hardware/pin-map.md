# Provisional Arduino Uno R3 pin map

| Function | Proposed pin | Notes |
|---|---|---|
| Left motor IN1/IN2 | D7 / D8 | Digital direction outputs |
| Left motor enable/PWM | D5 | PWM-capable |
| Right motor IN1/IN2 | D9 / D10 | Digital direction outputs |
| Right motor enable/PWM | D6 | PWM-capable |
| Ultrasonic trigger | D2 | Only if HC-SR04 is selected |
| Ultrasonic echo | D3 | 5 V echo is suitable for Uno input; verify actual sensor |
| Start button | D4 | Use defined pull-up/down and debounce |
| Debug serial | D0/D1 | Avoid for other functions while using USB serial |

This is a proposed mapping conditional on selecting an HC-SR04-style sensor and a compatible L293D breakout. It is not final until the sensor and driver pin labels are confirmed. If using I2C or another range sensor, update the map. Ensure driver enable pins default to disabled at reset.
