import requests
import tarfile

def download(filepath: str, url: str) -> None:
    with open(filepath, "wb") as file:
        file.write(requests.get(url).content)

def extract(archive: str, destination: str) -> None:
    with tarfile.open(archive, "r:*") as tar:
        tar.extractall(path=destination)