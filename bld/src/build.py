import os
import shutil
import install_libraries
from util import lua
from util import clang

def mkDir(name: str) -> str:
    os.mkdir(name)
    return name

if __name__ == "__main__":
    install_libraries.main()

    outDir: str = "bld/out"

    if not os.path.exists(outDir):
        os.mkdir(outDir)

    releaseDir: str = mkDir(f"{outDir}/Lyra")
    objDir: str = mkDir(f"{outDir}/obj")
    binDir: str = mkDir(f"{releaseDir}/bin")
    licenseDir: str = mkDir(f"{releaseDir}/lic")

    flags: dict = lua.parseFile("bld/cfg/flags.lua")
    general: dict = lua.parseFile("bld/cfg/general.lua")
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

    print(f"Transferring Lyra License...")
    shutil.copy (
        general["License"]["Source"],
        f"{licenseDir}/{general["License"]["OutName"]}"
    )

    print(f"Transferring Launcher Script...")
    shutil.copy (
        f"src/{general["Launcher"]["Linux"]["Source"]}",
        f"{releaseDir}/{general["Launcher"]["Linux"]["OutName"]}"
    )

    print("\n- Done! -")