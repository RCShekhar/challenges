from typing import Optional


def get_value(obj: dict, key:str)-> Optional[str]:
    value = obj
    if not key:
        return value #returns object iself if there is no key
    try:
        keys = key.split('/')
        for k in keys:
            value = value[k]
    except KeyError:
        print("Invalid Key", k)
        return None # Incase of key error returns None
    return value


