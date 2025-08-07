#pragma once

namespace lyra {
    class Vector2D {
    public:
        Vector2D();
        Vector2D(float x, float y);
        ~Vector2D() = default;

        float getX() const;
        float getY() const;

        virtual void setX(float value) const;
        virtual void setY(float value) const;
        virtual void set(float x, float y) const;

        virtual void incX(float value) const;
        virtual void incY(float value) const;
        virtual void inc(float x, float y) const;

        virtual void decX(float value) const;
        virtual void decY(float value) const;
        virtual void dec(float x, float y) const;

    private:
        mutable float _x;
        mutable float _y;
    };
}