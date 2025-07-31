import os
import shutil
from util import lua
from util import library

def main() -> None:
    thirdDir: str = "3rd"

    if os.path.exists(thirdDir):
        shutil.rmtree(thirdDir)
    os.mkdir(thirdDir)

    libs: dict = lua.parseFile("bld/cfg/libraries.lua")

    for lib in libs["Linux"]["External"]:
        print(f"Installing: {lib["URL"]}...")
        archive = f"{thirdDir}/{lib["URL"].replace("/", "")}"
        library.download(archive, lib["URL"])
        library.extract(archive, thirdDir)
        os.remove(archive)

    print("\n- Done! -")

if __name__ == "__main__": main()