from lupa import LuaRuntime, lua_type

def _isList(data: dict) -> bool:
    keys: list = list(data.keys())

    # Ensures all keys are of type int
    for key in keys:
        if not isinstance(key, int):
            return False

    # List of consecutive integers from 1 to number of keys
    expected: list = list(range(1, len(keys) + 1))

    return sorted(keys) == expected

def _dict2list(data: dict) -> list:
    return [data[key] for key in sorted(data, key=int)]

def _dicts2lists(data: dict, level=0) -> dict:
    newData: dict = {}

    for key, value in data.items():
        if lua_type(value) == "table":
            if _isList(value):
                newData[key] = _dict2list(_dicts2lists(value, level+1))
            else:
                newData[key] = _dicts2lists(value, level+1)
        else:
            newData[key] = value

    return newData

def parseFile(file: str) -> dict | list:
    data = _dicts2lists (
        LuaRuntime(unpack_returned_tuples=True).execute(f"return loadfile('{file}')")()
    )
    return _dict2list(data) if _isList(data) else dict(data)