import os
import shutil

def _join(strings: list[str]) -> str:
    return " ".join(f"{s}" for s in strings)

def build (
        objectDir: str,
        binDir: str,
        licenseDir: str,
        binName: str,
        libraries: list[dict],
        sources: list[str],
        compileFlags: list[str],
        linkFlags: list[str]
) -> None:
    objects: list[str] = []
    libIncludes: list[str] = []
    libPaths: list[str] = []
    libBins: list[str] = []

    for lib in libraries:
        for i in lib["Includes"]: libIncludes.append(f"-I3rd/{i}")
        for b in lib["Binaries"]:
            path, slash, bin = str(b).rpartition("/")
            libPaths.append(f"-L3rd/{path}")
            libBins.append(f"-l:{bin}")

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

    print(f"Transferring library Binaries & Licenses...")
    for lib in libraries:
        shutil.copy(f"3rd/{lib["License"]["Source"]}", f"{licenseDir}/{lib["License"]["OutName"]}")

        for bin in lib["Binaries"]:
            shutil.copy(f"3rd/{bin}", f"{binDir}/{os.path.basename(bin)}")
    return