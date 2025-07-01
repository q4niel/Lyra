import os
from datetime import datetime
from util import lua
from util import clang

if __name__ == "__main__":
    outDir: str = "bld/out"
    buildDir: str = f"{outDir}/{datetime.now().strftime("latest_%H_%M_%S_%f")}"
    objDir: str = f"{buildDir}/obj"

    if not os.path.exists(outDir):
        os.mkdir(outDir)

    for name in os.listdir(outDir):
        if name.startswith("latest_"):
            os.rename(f"{outDir}/{name}", f"{outDir}/{name[7:]}")
            break

    os.mkdir(buildDir)
    os.mkdir(objDir)

    flags: dict = lua.parseFile("bld/cfg/flags.lua")
    version: dict = lua.parseFile("bld/cfg/version.lua")
    sources: list = lua.parseFile("bld/cfg/sources.lua")

    clang.build (
        "lyra",
        objDir,
        sources,
        objDir,
        flags["Compilation"],
        flags["Linking"]
    )