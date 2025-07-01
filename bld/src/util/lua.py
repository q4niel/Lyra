from lupa import LuaRuntime, lua_type

def parseFile(file: str) -> dict | list:
    def isList(data: dict) -> bool:
        keys: list = list(data.keys())

        # Ensures all keys are of type int
        for key in keys:
            if not isinstance(key, int):
                return False

        # List of consecutive integers from 1 to number of keys
        expected: list = list(range(1, len(keys) + 1))

        return sorted(keys) == expected

    def dict2list(data: dict) -> list:
        return [data[key] for key in sorted(data, key=int)]

    def dicts2lists(data: dict, level=0) -> dict:
        newData: dict = {}

        for key, value in data.items():
            if lua_type(value) == "table":
                if isList(value):
                    newData[key] = dict2list(value)
                else:
                    newData[key] = dicts2lists(value, level+1)
            else:
                newData[key] = value

        return newData

    data = dicts2lists (
        LuaRuntime(unpack_returned_tuples=True).execute(f"return loadfile('{file}')")()
    )
    return dict2list(data) if isList(data) else dict(data)