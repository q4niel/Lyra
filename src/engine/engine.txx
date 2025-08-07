#pragma once

template<lyra::DerivedFromElement2D T, typename... Args>
void lyra::Engine::addElement(Args&&... args) {
    _elements.emplace_back (
        new T(std::forward<Args>(args)...)
    );
}