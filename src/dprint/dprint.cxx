#include "dprint.hxx"
#include <iostream>

void __dprint__::__printSpace__(unsigned int count) {
    for (int i = 0; i < count; i++) {
        std::cout << '\n';
    }
}