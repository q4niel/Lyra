#include "dprint.hxx"

template<typename T, typename ...Args>
void dprint::__print__(T t, Args ...args) {
    std::cout << t;
    if constexpr (sizeof ...(Args) > 0) {
        dprint::__print__(args...);
    }
}