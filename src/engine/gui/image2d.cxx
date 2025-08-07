#include "image2d.hxx"

lyra::Image2D::Image2D(std::string texturePath) :
    lyra::Element2D::Element2D(),
    _texture(LoadTexture(texturePath.c_str()))
{}

lyra::Image2D::~Image2D() {
    UnloadTexture(_texture);
}

const Texture2D &lyra::Image2D::getTexture() {
    return _texture;
}