import requests
import tarfile
import os

def download(filepath: str, url: str) -> None:
    with open(filepath, "wb") as file:
        file.write(requests.get(url).content)

def extract(archive: str, destination: str) -> None:
    with tarfile.open(archive, "r:*") as tar:
        tar.extractall(path=destination)

class SystemLicenseBuilder:
    def __init__(self, name: str, filepath: str):
        self.name: str = name
        self.filepath: str = f"{filepath}/{name}"
        self.binaries: list[str] = []
        self.content: str = ""

    def addBinary(self, binName: str):
        self.binaries.append(os.path.basename(binName))

    def addContent(self, string: str):
        self.content += string

    def build(self) -> bool:
        if not self.binaries:
            print(f"Cannot build license: {self.name}, 'self.binaries' list is empty.")
            return False

        print(f"building {self.name} with binaries:")
        for bin in self.binaries:
            print(f"    {bin}")
            self.content += f"\n- {bin}"

        with open(self.filepath, "wb") as file:
            file.write(self.content.encode())
        return True