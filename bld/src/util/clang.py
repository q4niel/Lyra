import os

def compile(source: str, outDir: str, flags: list[str]) -> None:
    allFlags: str = " ".join(f"{flag}" for flag in flags)
    os.system(f"clang++ {allFlags} -c src/{source} -o {outDir}/{os.path.basename(source)[:-4]}.o")