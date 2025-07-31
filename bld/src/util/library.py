import requests
import tarfile
import os
from typing import Optional

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
        self.notice: Optional[str] = None
        self.binaries: list[str] = []
        self.license: Optional[str] = None
        self.content: str = ""

    def addNotice(self, string: str) -> None:
        self.notice = string

    def addBinary(self, binName: str) -> None:
        self.binaries.append(os.path.basename(binName))

    def addLicense(self, string: str) -> None:
        self.license = string

    def build(self) -> None:
        errorPrefix: str = f"Cannot build license {self.name}: "

        if self.notice is None:
            print(f"{errorPrefix}'self.notice' is None")
            return
        self.content += self.notice

        if not self.binaries:
            print(f"{errorPrefix}'self.binaries' list is empty")
            return

        print(f"building {self.name} with binaries:")
        for bin in self.binaries:
            print(f"    {bin}")
            self.content += f"\n- {bin}"

        if self.license is None:
            print(f"{errorPrefix}'self.license' is None")
            return
        self.content += f"\n\n\n\n{self.license}"

        with open(self.filepath, "wb") as file:
            file.write(self.content.encode())
        return