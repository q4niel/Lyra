#pragma once
#include <optional>
#include <vector>
#include <type_traits>
#include "gui/base/element2d.hxx"

#ifdef DEBUG
    #include <expected>
    #include <string>
    #define EXPECT_TYPE(T) std::expected<T, std::string>
    #define EXPECT_TYPE_ERROR(MSG) std::unexpected(MSG)
    #define EXPECT_VOID std::expected<void, std::string>
    #define EXPECT_VOID_ERROR(MSG) std::unexpected(MSG)
    #define EXPECT_VOID_SUCCESS {}
#else
    #define EXPECT_TYPE(T) std::optional<T>
    #define EXPECT_TYPE_ERROR(MSG) std::nullopt
    #define EXPECT_VOID bool
    #define EXPECT_VOID_ERROR(MSG) false
    #define EXPECT_VOID_SUCCESS true
#endif

namespace lyra {
    template<typename T>
    concept DerivedFromElement2D = std::derived_from<T, Element2D>;

    class Engine {
    private: struct InitTag { explicit InitTag() = default; };

    public:
        Engine(struct InitTag);
        ~Engine();

        static std::optional<Engine*> instance();
        static EXPECT_TYPE(Engine) create();
        EXPECT_VOID init();
        EXPECT_VOID process();

        template<DerivedFromElement2D T, typename... Args>
        const T *const instantiateElement(Args&&... args);

        Engine(const Engine&) = delete;            // Engine e2 = e1; (copy construction)
        Engine& operator=(const Engine&) = delete; // e2 = e1; (copy assignment)
        Engine(Engine&&) = delete;                 // Engine e2 = std::move(e1); (move construction)
        Engine& operator=(Engine&&) = delete;      // e2 = std::move(e1); (move assignment)

    private:
        bool _isInitialized;
        std::vector<Element2D*> _elements;

        Engine();
        float _clampf(float value, float min, float max);
        void _drawElements();
        void _clean();
    };
}

#include "engine.txx"