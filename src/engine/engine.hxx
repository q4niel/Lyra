#pragma once
#include <optional>
#include <expected>
#include <string>

namespace lyra {
    class Engine {
    private:
        Engine();
        struct InitTag { explicit InitTag() = default; };
        bool isInitialized;

    public:
        static std::expected<Engine, std::string> create();
        static std::optional<Engine*> instance();

        std::expected<void, std::string> init();
        std::expected<void, std::string> process();
        void clean();

        Engine(struct InitTag);
        ~Engine();

        Engine(const Engine&) = delete;            // Engine e2 = e1; (copy construction)
        Engine& operator=(const Engine&) = delete; // e2 = e1; (copy assignment)
        Engine(Engine&&) = delete;                 // Engine e2 = std::move(e1); (move construction)
        Engine& operator=(Engine&&) = delete;      // e2 = std::move(e1); (move assignment)
    };
}