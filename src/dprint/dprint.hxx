#pragma once

#ifdef DEBUG
    #include <iostream>
    #include <utility>

    #define flushConsole std::cout << std::flush

    // Prints all arguments consecutively, no newline.
    #define print(...) __dprint__::__print__(__VA_ARGS__)

    // Prints all arguments consecutively, followed by newline.
    #define println(...) __dprint__::__println__(__VA_ARGS__)

    // Prints each argument followed by newline.
    #define printlns(...) __dprint__::__printlns__(__VA_ARGS__)

    // Prints newlines; count = number of lines (default: 1).
    #define printSpace(count) __dprint__::__printSpace__(count)

    namespace __dprint__ {
        // Internal helper; use the `print` macro instead.
        template<typename... Args>
        void __print__(Args&&... args);

        // Internal helper; use the `println` macro instead.
        template<typename... Args>
        void __println__(Args&&... args);

        // Internal helper; use the `printlns` macro instead.
        template<typename... Args>
        void __printlns__(Args&&... args);

        // Internal helper; use the `printSpace` macro instead.
        void __printSpace__(unsigned int count = 1);
    }

    #include "dprint.txx"
#else
    #define flushConsole
    #define print(...)
    #define println(...)
    #define printlns(...)
    #define printSpace(count)
#endif