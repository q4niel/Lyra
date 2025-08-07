#pragma once

template<lyra::DerivedFromElement2D T, typename... Args>
const T *const lyra::Engine::instantiateElement(Args&&... args) {
    _elements.emplace_back (
        new T(std::forward<Args>(args)...)
    );

    return (const T *const)_elements.back();
}