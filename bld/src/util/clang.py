import os
import sys
import shutil
import requests
from typing import Final
from . import library

def _join(strings: list[str]) -> str:
    return " ".join(f"{s}" for s in strings)

def build (
        objectDir: str,
        binDir: str,
        licenseDir: str,
        binName: str,
        libraries: dict,
        sources: dict,
        compileFlags: list[str],
        linkFlags: list[str]
) -> None:
    debugMode_: Final[bool] = "-DDEBUG" in sys.argv

    objects: list[str] = []
    libIncludes: list[str] = []
    libPaths: list[str] = []
    libBins: list[str] = []
    sysLibLics: dict[str, library.SystemLicenseBuilder] = {}

    for lic in libraries["System"]["Licenses"]:
        sysLibLics[lic["Name"]] = library.SystemLicenseBuilder(lic["Name"], licenseDir)
        sysLibLics[lic["Name"]].addNotice(libraries["System"]["LicenseBinaryNotice"])
        sysLibLics[lic["Name"]].addLicense(requests.get(lic["License"]).text)

    def addLibBin(path: str) -> None:
        dir, slash, bin = str(path).rpartition("/")
        libPaths.append(f"-L3rd/{dir}")
        libBins.append(f"-l:{bin}")

    for lib in libraries["External"]:
        for i in lib["Includes"]: libIncludes.append(f"-I3rd/{i}")
        for b in lib["Binaries"]: addLibBin(b)

    for lib in libraries["System"]["Binaries"]:
        addLibBin(bin:= lib["Binary"])
        for lic in lib["Licenses"]:
            if lic in sysLibLics:
                sysLibLics[lic].addBinary(bin)
            else:
                print(f"License '{lic}' for '{bin}' is undefined.")

    def compileSource(src: str) -> None:
        obj: str = f"{os.path.basename(src).rsplit(".", 1)[0]}.o"
        print(f"Compiling {src}...")
        os.system(f"clang++ -Qunused-arguments {"-DDEBUG" if debugMode_ else ""} {_join(compileFlags)} {_join(libIncludes)} -c src/{src} -o {objectDir}/{obj}")
        objects.append(f"{objectDir}/{obj}")

    ext: str
    for src in sources["Release"]["Universal"]: compileSource(src)
    if debugMode_:
        for src in sources["DebugOnly"]["Universal"]: compileSource(src)

    match os.name:
        case "nt":
            ext = ".exe"
            for src in sources["Release"]["Windows"]: compileSource(src)
            if debugMode_:
                for src in sources["DebugOnly"]["Windows"]: compileSource(src)
        case "posix":
            ext = ""
            for src in sources["Release"]["Linux"]: compileSource(src)
            if debugMode_:
                for src in sources["DebugOnly"]["Linux"]: compileSource(src)
        case _:
            return

    print(f"Linking sources...")
    os.system(f"clang++ {"-DDEBUG" if debugMode_ else ""} {_join(libPaths)} {_join(libBins)} {_join(objects)} -o {binDir}/{binName}{ext} {_join(linkFlags)}")

    print(f"Transferring System Library Binaries...")
    for lib in libraries["System"]["Binaries"]:
        shutil.copy(lib["Binary"], f"{binDir}/{os.path.basename(lib["Binary"])}")

        if lib["Symlink"]:
            oldCWD: str = os.getcwd()
            os.chdir(binDir)
            os.symlink(os.path.basename(lib["Binary"]), lib["Symlink"])
            os.chdir(oldCWD)

    print(f"Building System Library Licenses...")
    for name, lic in sysLibLics.items(): lic.build()

    print(f"Transferring External Library Binaries & Licenses...")
    for lib in libraries["External"]:
        shutil.copy(f"3rd/{lib["License"]["Source"]}", f"{licenseDir}/{lib["License"]["OutName"]}")

        for bin in lib["Binaries"]:
            shutil.copy(f"3rd/{bin}", f"{binDir}/{os.path.basename(bin)}")
    return