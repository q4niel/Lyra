return {
    DebugOnly = {
        Linux = {},
        Windows = {},
        Universal = {}
    },
    Release = {
        Linux = {
            "entry/linux_x86-64_start.s"
        },
        Windows = {},
        Universal = {
            "entry/main.cxx"
        }
    }
}