return {
    DebugOnly = {
        Linux = {},
        Windows = {},
        Universal = {
            "dprint/dprint.cxx"
        }
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