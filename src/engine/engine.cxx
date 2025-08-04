#include <raylib.h>
#include "engine.hxx"
#include "../dprint/dprint.hxx"

namespace lyra {
    static Engine *instPtr = nullptr;

    std::expected<Engine, std::string> Engine::create() {
        if (lyra::instPtr != nullptr) {
            return std::unexpected("Failed to create Engine: another instance is already active.");
        }
        return std::expected<lyra::Engine, std::string>{std::in_place, InitTag{}};
    }

    std::optional<Engine*> Engine::instance() {
        if (lyra::instPtr == nullptr) {
            return std::nullopt;
        }
        return lyra::instPtr;
    }

    std::expected<void, std::string> Engine::init() {
        SetTraceLogLevel(LOG_NONE);
        SetConfigFlags(FLAG_WINDOW_RESIZABLE);
        InitWindow(800, 600, "My Window");

        if (!IsWindowReady()) return std::unexpected("Failed to initialize Engine.");

        #ifndef DEBUG
            SetExitKey(KEY_NULL);
        #endif

        SetTargetFPS(60);
        isInitialized = true;
        return {};
    }

    std::expected<void, std::string> Engine::process() {
        if (WindowShouldClose()) return std::unexpected("Engine Process: closed by window.");

        BeginDrawing();
        ClearBackground(GRAY);
        EndDrawing();

        return {};
    }

    void Engine::clean() {
        if (!isInitialized) return;
        CloseWindow();
    }

    Engine::Engine(InitTag) :
        isInitialized(false)
    {
        println("Engine Constructed");
        lyra::instPtr = this;
    }

    Engine::~Engine() {
        println("Engine Destructed");
        clean();
        lyra::instPtr = nullptr;
    }
}