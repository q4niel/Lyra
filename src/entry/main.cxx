#include <cstdlib>
#include "../dprint/dprint.hxx"
#include "../engine/engine.hxx"

int main(int argc, char **argv) {
    if (!eng::init()) {
        println("Error: Engine initialization failed");
        return EXIT_FAILURE;
    }
    println("Engine initialization succeeded");

    while (eng::process()) {}

    if (!eng::shutdown()) {
        println("Error: Engine shutdown failed");
        return EXIT_FAILURE;
    }
    println("Engine shutdown succeeded");
    return EXIT_SUCCESS;
}