return {
    Linux = {
        System = {
            LicenseBinaryNotice = "This document applies to the following distributed binaries:",
            Licenses = {
                {Name = "LGPLv3", Type = "TEXT", URL = "https://www.gnu.org/licenses/lgpl-3.0.txt"},
                {Name = "GPLv3", Type = "TEXT", URL = "https://www.gnu.org/licenses/gpl-3.0.txt"},
                {Name = "GCCEv3.1", Type = "HTML", URL = "https://www.gnu.org/licenses/gcc-exception-3.1.html"}
            },
            Binaries = {
                {
                    Licenses = {"LGPLv3"},
                    Binary = "/usr/lib64/ld-linux-x86-64.so.2",
                    Symlink = false
                },
                {
                    Licenses = {"LGPLv3"},
                    Binary = "/usr/lib/libm.so.6",
                    Symlink = false
                },
                {
                    Licenses = {"LGPLv3"},
                    Binary = "/usr/lib/libc.so.6",
                    Symlink = false
                },
                {
                    Licenses = {"LGPLv3"},
                    Binary = "/usr/lib/libpthread.so.0",
                    Symlink = false
                },
                {
                    Licenses = {"LGPLv3"},
                    Binary = "/usr/lib/libdl.so.2",
                    Symlink = false
                },
                {
                    Licenses = {"GPLv3", "GCCEv3.1"},
                    Binary = "/usr/lib/libstdc++.so.6.0.34",
                    Symlink = "libstdc++.so.6"
                },
                {
                    Licenses = {"GPLv3", "GCCEv3.1"},
                    Binary = "/usr/lib/libgcc_s.so.1",
                    Symlink = false
                }
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