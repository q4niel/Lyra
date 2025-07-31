return {
    Linux = {
        System = {
            LicenseBinaryNotice = "This document applies to the following distributed binaries:",
            Licenses = {
                {Name = "LGPL-2.1-or-later", License = "https://raw.githubusercontent.com/spdx/license-list-data/main/text/LGPL-2.1-or-later.txt"},
                {Name = "GPL-3.0-only", License = "https://raw.githubusercontent.com/spdx/license-list-data/main/text/GPL-3.0-only.txt"},
                {Name = "GCC-exception-3.1", License = "https://raw.githubusercontent.com/spdx/license-list-data/main/text/GCC-exception-3.1.txt"}
            },
            Binaries = {
                {
                    Licenses = {"LGPL-2.1-or-later"},
                    Binary = "/usr/lib64/ld-linux-x86-64.so.2",
                    Symlink = false
                },
                {
                    Licenses = {"LGPL-2.1-or-later"},
                    Binary = "/usr/lib/libm.so.6",
                    Symlink = false
                },
                {
                    Licenses = {"LGPL-2.1-or-later"},
                    Binary = "/usr/lib/libc.so.6",
                    Symlink = false
                },
                {
                    Licenses = {"LGPL-2.1-or-later"},
                    Binary = "/usr/lib/libpthread.so.0",
                    Symlink = false
                },
                {
                    Licenses = {"LGPL-2.1-or-later"},
                    Binary = "/usr/lib/libdl.so.2",
                    Symlink = false
                },
                {
                    Licenses = {"GPL-3.0-only", "GCC-exception-3.1"},
                    Binary = "/usr/lib/libstdc++.so.6.0.34",
                    Symlink = "libstdc++.so.6"
                },
                {
                    Licenses = {"GPL-3.0-only", "GCC-exception-3.1"},
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