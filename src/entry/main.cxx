#include <cstdlib>
#include "../dprint/dprint.hxx"
#include "../engine/engine.hxx"

int main(int argc, char **argv) {
    if (!lyra::Engine::init()) {
        println("Error: Engine initialization failed");
        return EXIT_FAILURE;
    }
    println("Engine initialization succeeded");

    while (lyra::Engine::process()) {}

    if (!lyra::Engine::shutdown()) {
        println("Error: Engine shutdown failed");
        return EXIT_FAILURE;
    }

    println("Engine shutdown succeeded");
    return EXIT_SUCCESS;
}