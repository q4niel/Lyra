#pragma once
#include "base/element2d.hxx"
#include <string>
#include <raylib.h>

namespace lyra {
    class Image2D : public Element2D {
    public:
        Image2D() = delete;
        Image2D(std::string texturePath);
        ~Image2D();

        const Texture2D &getTexture();

    private:
        Texture2D _texture;
    };
}