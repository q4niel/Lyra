import os
import shutil
from . import library

def _join(strings: list[str]) -> str:
    return " ".join(f"{s}" for s in strings)

def build (
        objectDir: str,
        binDir: str,
        licenseDir: str,
        binName: str,
        libraries: dict,
        sources: list[str],
        compileFlags: list[str],
        linkFlags: list[str]
) -> None:
    objects: list[str] = []
    libIncludes: list[str] = []
    libPaths: list[str] = []
    libBins: list[str] = []
    sysLibLics: dict[str, library.SystemLicenseBuilder] = {
        lic["Name"]: library.SystemLicenseBuilder(lic["Name"], licenseDir)
        for lic in libraries["System"]["Licenses"]
    }

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

    for src in sources:
        obj: str = f"{os.path.basename(src)[:-4]}.o"
        print(f"Compiling {src}...")
        os.system(f"clang++ {_join(compileFlags)} {_join(libIncludes)} -c src/{src} -o {objectDir}/{obj}")
        objects.append(f"{objectDir}/{obj}")

    ext: str

    match os.name:
        case "nt":
            ext = ".exe"
        case "posix":
            ext = ""
        case _:
            return

    print(f"Linking sources...")
    os.system(f"clang++ {_join(libPaths)} {_join(libBins)} {_join(objects)} -o {binDir}/{binName}{ext} {_join(linkFlags)}")

    print(f"Transferring System Library Binaries...")
    for lib in libraries["System"]["Binaries"]:
        shutil.copy(lib["Binary"], f"{binDir}/{os.path.basename(lib["Binary"])}")

        if lib["Symlink"]:
            oldCWD: str = os.getcwd()
            os.chdir(binDir)
            os.symlink(os.path.basename(lib["Binary"]), lib["Symlink"])
            os.chdir(oldCWD)

    print(f"Building System Library Licenses...")
    for name, lic in sysLibLics.items():
        lic.addContent(libraries["System"]["LicenseBinaryNotice"])
        lic.build()

    print(f"Transferring External Library Binaries & Licenses...")
    for lib in libraries["External"]:
        shutil.copy(f"3rd/{lib["License"]["Source"]}", f"{licenseDir}/{lib["License"]["OutName"]}")

        for bin in lib["Binaries"]:
            shutil.copy(f"3rd/{bin}", f"{binDir}/{os.path.basename(bin)}")
    return