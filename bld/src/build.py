import os
from datetime import datetime
from util import lua
from util import clang

if __name__ == "__main__":
    outDir: str = "bld/out"
    buildDir: str = f"{outDir}/{datetime.now().strftime("latest_%H_%M_%S_%f")}"
    cacheDir: str = f"{buildDir}/cache"

    if not os.path.exists(outDir):
        os.mkdir(outDir)

    for name in os.listdir(outDir):
        if name.startswith("latest_"):
            os.rename(f"{outDir}/{name}", f"{outDir}/{name[7:]}")
            break

    os.mkdir(buildDir)
    os.mkdir(cacheDir)

    flags: list = lua.parseList("bld/cfg/flags.lua")
    version: dict = lua.parseDict("bld/cfg/version.lua")
    sources: list = lua.parseList("bld/cfg/sources.lua")

    for src in sources:
        clang.compile(src, cacheDir, flags)