#include "engine.hxx"
#include <raylib.h>

bool eng::init() {
    #ifndef DEBUG
        SetTraceLogLevel(LOG_NONE);
    #endif
    SetConfigFlags(FLAG_WINDOW_RESIZABLE);
    InitWindow(800, 600, "My Window");

    if (!IsWindowReady()) return false;

    SetTargetFPS(60);
    return true;
}

bool eng::process() {
    if (WindowShouldClose()) return false;

    BeginDrawing();
    ClearBackground(GRAY);
    EndDrawing();

    return true;
}

bool eng::shutdown() {
    CloseWindow();
    return true;
}