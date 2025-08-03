#pragma once

namespace lyra {
    class Engine {
    public:
        Engine() = delete;

        static bool init();
        static bool shutdown();
        static bool process();
    };
}