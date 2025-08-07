#include "vector2d.hxx"

lyra::Vector2D::Vector2D() : _x(0), _y(0) {}
lyra::Vector2D::Vector2D(float x, float y) : _x(x), _y(y) {}

float lyra::Vector2D::getX() const { return _x; }
float lyra::Vector2D::getY() const { return _y; }

void lyra::Vector2D::setX(float value) const { _x = value; }
void lyra::Vector2D::setY(float value) const { _y = value; }
void lyra::Vector2D::set(float x, float y) const {
    _x = x;
    _y = y;
}


void lyra::Vector2D::incX(float value) const { _x += value; }
void lyra::Vector2D::incY(float value) const { _y += value; }
void lyra::Vector2D::inc(float x, float y) const {
    _x += x;
    _y += y;
}

void lyra::Vector2D::decX(float value) const { _x -= value; }
void lyra::Vector2D::decY(float value) const { _y -= value; }
void lyra::Vector2D::dec(float x, float y) const {
    _x -= x;
    _y -= y;
}