#include <raylib.h>
#include "engine.hxx"
#include "../dprint/dprint.hxx"

namespace lyra {
    static Engine *instPtr = nullptr;

    std::optional<Engine*> Engine::instance() {
        if (lyra::instPtr == nullptr) {
            return std::nullopt;
        }
        return lyra::instPtr;
    }

    EXPECT_TYPE(Engine) Engine::create() {
        if (lyra::instPtr != nullptr) {
            return EXPECT_TYPE_ERROR("Failed to create Engine: another instance is already active.");
        }
        return EXPECT_TYPE(Engine){std::in_place, InitTag{}};
    }

    EXPECT_VOID Engine::init() {
        SetTraceLogLevel(LOG_NONE);
        SetConfigFlags(FLAG_WINDOW_RESIZABLE);
        InitWindow(800, 600, "My Window");

        if (!IsWindowReady()) return EXPECT_VOID_ERROR("Failed to initialize Engine.");

        #ifndef DEBUG
            SetExitKey(KEY_NULL);
        #endif

        SetTargetFPS(60);
        _isInitialized = true;
        return EXPECT_VOID_SUCCESS;
    }

    EXPECT_VOID Engine::process() {
        if (WindowShouldClose()) return EXPECT_VOID_ERROR("Engine Process: closed by window.");

        BeginDrawing();
        ClearBackground(GRAY);
        EndDrawing();

        return EXPECT_VOID_SUCCESS;
    }

    void Engine::_clean() {
        if (!_isInitialized) return;
        CloseWindow();
    }

    Engine::Engine(InitTag) :
        _isInitialized(false)
    {
        println("Engine Constructed");
        lyra::instPtr = this;
    }

    Engine::~Engine() {
        println("Engine Destructed");
        _clean();
        lyra::instPtr = nullptr;
    }
}