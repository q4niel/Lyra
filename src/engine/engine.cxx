#include <raylib.h>
#include "engine.hxx"

namespace lyra {
    bool Engine::init() {
        #ifndef DEBUG
            SetTraceLogLevel(LOG_NONE);
        #endif

        SetConfigFlags(FLAG_WINDOW_RESIZABLE);
        InitWindow(800, 600, "My Window");

        if (!IsWindowReady()) return false;

        #ifndef DEBUG
            SetExitKey(KEY_NULL);
        #endif

        SetTargetFPS(60);
        return true;
    }

    bool Engine::shutdown() {
        CloseWindow();
        return true;
    }

    bool Engine::process() {
        if (WindowShouldClose()) return false;

        BeginDrawing();
        ClearBackground(GRAY);
        EndDrawing();

        return true;
    }
}