#include "element2d.hxx"

lyra::Element2D::Element2D() : _enabled(true) {}

void lyra::Element2D::enable() { _enabled = true; }
void lyra::Element2D::disable() { _enabled = false; }
bool lyra::Element2D::isEnabled() { return _enabled; }