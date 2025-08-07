#pragma once

#define __PRINT_ARGS__(...) \
((std::cout << std::forward<Args>(args) __VA_OPT__(<< __VA_ARGS__) ), ...)

template<typename... Args>
void __dprint__::__print__(Args&&... args) {
    __PRINT_ARGS__();
}

template<typename... Args>
void __dprint__::__println__(Args&&... args) {
    __PRINT_ARGS__();
    std::cout << '\n';
}

template<typename... Args>
void __dprint__::__printlns__(Args&&... args) {
    __PRINT_ARGS__('\n');
}

#undef __PRINT_ARGS__