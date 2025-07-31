#include "dprint.hxx"

void dprint::__printSpace__(unsigned int count) {
    for (int i = 0; i < count; i++) {
        std::cout << '\n';
    }
}