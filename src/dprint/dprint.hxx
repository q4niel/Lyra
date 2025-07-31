#pragma once

#ifdef DEBUG
    #include <iostream>

    namespace dprint {
        template<typename T, typename ...Args>
        void __print__(T t, Args ...args);

        void __printSpace__(unsigned int count = 1);
    }

    #define print(...) dprint::__print__(__VA_ARGS__)
    #define printSpace(count) dprint::__printSpace__(count)
    #define FLUSH std::cout << std::flush
    #include "dprint.txx"
#else
    #define print(...)
    #define printSpace(count)
    #define FLUSH
#endif