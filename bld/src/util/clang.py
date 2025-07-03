import os

def _join(strings: list[str]) -> str:
    return " ".join(f"{s}" for s in strings)

def build(binName: str, outDir: str, libraries: list[dict], sources: list[str], objectDir: str, compileFlags: list[str], linkFlags: list[str]) -> None:
    objects: list[str] = []
    libIncludes: list[str] = []
    libPaths: list[str] = []
    libBins: list[str] = []

    for lib in libraries:
        for i in lib["Includes"]: libIncludes.append(f"-I3rd/{i}")
        for p in lib["Paths"]: libPaths.append(f"-L3rd/{p}")
        for b in lib["Binaries"]: libBins.append(f"-l:{b}")

    for src in sources:
        obj: str = f"{os.path.basename(src)[:-4]}.o"
        print(f"Compiling {src}...")
        cmd: str = f"clang++ {_join(compileFlags)} {_join(libIncludes)} -c src/{src} -o {objectDir}/{obj}"
        os.system(cmd)
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
    cmd:str = f"clang++ {_join(linkFlags)} {_join(libPaths)} {_join(libBins)} {_join(objects)} -o {outDir}/{binName}{ext} -Wl,-rpath,'$ORIGIN'"
    os.system(cmd)
    return