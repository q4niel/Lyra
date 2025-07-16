return {
    Linux = {
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