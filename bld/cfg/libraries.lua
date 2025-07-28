return {
    Linux = {
        System = {
            {
                License = "",
                Binary = "/usr/lib64/ld-linux-x86-64.so.2",
                Symlink = false
            },
            {
                License = "",
                Binary = "/usr/lib/libstdc++.so.6.0.34",
                Symlink = "libstdc++.so.6"
            },
            {
                License = "",
                Binary = "/usr/lib/libm.so.6",
                Symlink = false
            },
            {
                License = "",
                Binary = "/usr/lib/libgcc_s.so.1",
                Symlink = false
            },
            {
                License = "",
                Binary = "/usr/lib/libc.so.6",
                Symlink = false
            },
            {
                License = "",
                Binary = "/usr/lib/libpthread.so.0",
                Symlink = false
            },
            {
                License = "",
                Binary = "/usr/lib/libdl.so.2",
                Symlink = false
            }
        },
        External = {
            {
                URL = "https://github.com/raysan5/raylib/releases/download/5.5/raylib-5.5_linux_amd64.tar.gz",
                License = {
                    Source = "raylib-5.5_linux_amd64/LICENSE",
                    OutName = "libraylib.so.550_LICENSE"
                },
                Includes = {"raylib-5.5_linux_amd64/include"},
                Binaries = {"raylib-5.5_linux_amd64/lib/libraylib.so.550"}
            }
        }
    }
}