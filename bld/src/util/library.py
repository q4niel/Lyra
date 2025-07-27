import requests
import tarfile
import subprocess

def download(filepath: str, url: str) -> None:
    with open(filepath, "wb") as file:
        file.write(requests.get(url).content)

def extract(archive: str, destination: str) -> None:
    with tarfile.open(archive, "r:*") as tar:
        tar.extractall(path=destination)

def getSystemLibPaths() -> list[str]:
    deps: list[str] = subprocess.run(["ldd", "bld/out/Lyra/bin/lyra"], capture_output=True, text=True).stdout.splitlines()
    paths: list[str] = []

    for line in deps:
        parts = line.split('=>')
        if len(parts) == 2:

            # Right side contains path + address
            right = parts[1].strip()

            # Path is the first token before space or '('
            path = right.split()[0]

            if path.startswith("/Lyra"):
                pass
            elif path.startswith("/"):
                paths.append(path)
        else:
            pass

    return paths