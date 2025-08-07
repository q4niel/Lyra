#pragma once
#include "transform2d.hxx"

namespace lyra {
    class Element2D {
    public:
        const Transform2D transform;

        Element2D();
        virtual ~Element2D() = default;
        void enable();
        void disable();
        bool isEnabled();

    private:
        bool _enabled;
    };
}