import os

def _join(strings: list[str]) -> str:
    return " ".join(f"{s}" for s in strings)

def build(binName: str, outDir: str, sources: list[str], objectDir: str, compileFlags: list[str], linkFlags: list[str]) -> None:
    objects: list[str] = []

    for src in sources:
        obj: str = f"{os.path.basename(src)[:-4]}.o"
        os.system(f"clang++ {_join(compileFlags)} -c src/{src} -o {objectDir}/{obj}")
        objects.append(f"{objectDir}/{obj}")

    ext: str

    match os.name:
        case "nt":
            ext = ".exe"
        case "posix":
            ext = ""
        case _:
            return

    os.system(f"clang++ {_join(linkFlags)} {_join(objects)} -o {outDir}/{binName}{ext}")
    return