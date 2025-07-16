import os
from datetime import datetime
from util import lua
from util import clang

def mkDir(name: str) -> str:
    os.mkdir(name)
    return name

if __name__ == "__main__":
    outDir: str = "bld/out"

    if not os.path.exists(outDir):
        os.mkdir(outDir)

    for name in os.listdir(outDir):
        if name.startswith("latest_"):
            os.rename(f"{outDir}/{name}", f"{outDir}/{name[7:]}")
            break

    buildDir: str = mkDir(f"{outDir}/{datetime.now().strftime("latest_%H_%M_%S_%f")}")
    releaseDir: str = mkDir(f"{buildDir}/Lyra")
    objDir: str = mkDir(f"{buildDir}/obj")
    binDir: str = mkDir(f"{releaseDir}/bin")
    licenseDir: str = mkDir(f"{releaseDir}/lic")

    flags: dict = lua.parseFile("bld/cfg/flags.lua")
    version: dict = lua.parseFile("bld/cfg/version.lua")
    libraries: list = lua.parseFile("bld/cfg/libraries.lua")
    sources: list = lua.parseFile("bld/cfg/sources.lua")

    clang.build (
        objDir,
        binDir,
        licenseDir,
        "lyra",
        libraries["Linux"],
        sources,
        flags["Compilation"],
        flags["Linking"]
    )

    print("\n- Done! -")