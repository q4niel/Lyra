return {
    Compilation = {
        "-std=c++23"
    },
    Linking = {
        "-nostdlib",
        "-nodefaultlibs",
        "-nostartfiles",
        "-Wl,-rpath,'$ORIGIN'"
    }
}