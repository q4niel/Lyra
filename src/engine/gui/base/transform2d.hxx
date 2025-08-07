#pragma once
#include "vector2d.hxx"

namespace lyra {
    struct Transform2D {
        const Vector2D position;
        const Vector2D rotation;
        const Vector2D scale;
    };
}