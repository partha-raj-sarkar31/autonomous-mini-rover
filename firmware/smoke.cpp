#include <iostream>
#include "rover_navigation.h"
int main() {
    rover::Navigator nav;
    rover::Input in = {true, true, 100.0f, 0};
    rover::Output out = nav.update(in);
    in.start = false; in.now_ms = 10;
    out = nav.update(in);
    std::cout << "state=" << static_cast<int>(out.state)
              << " motion=" << static_cast<int>(out.motion)
              << " fault=" << out.fault << "\n";
    return out.fault ? 1 : 0;
}
