from lupa import LuaRuntime

def parseDict(file: str) -> dict:
    return LuaRuntime(unpack_returned_tuples=True).execute(f"return loadfile('{file}')")()

def parseList(file: str) -> list:
    data: dict = parseDict(file)
    return [data[key] for key in sorted(data, key=int)]