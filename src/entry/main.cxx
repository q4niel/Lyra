#include <cstdlib>
#include <thread>
#include <chrono>
#include "../dprint/dprint.hxx"
#include "../engine/engine.hxx"

int main(int argc, char **argv) {
    auto engineCB = lyra::Engine::create();
    if (!engineCB) {
        println(engineCB.error());
        return EXIT_FAILURE;
    }

    auto initCB = engineCB->init();
    if (!initCB) {
        println(initCB.error());
        return EXIT_FAILURE;
    }

    int count = 0;
    while (true) {
        auto procCB = engineCB->process();
        if (!procCB) {
            println(procCB.error());
            break;
        }

        std::this_thread::sleep_for(std::chrono::seconds(1));
        count++;
        println(count);
    }

    return EXIT_SUCCESS;
}