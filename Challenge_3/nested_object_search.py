from typing import Optional


def get_value(obj: dict, key:str)-> Optional[str]:
    value = obj
    if not key:
        return value #returns object iself if there is no key
    try:
        keys = key.split('/')
        for k in keys:
            if type(value) != dict:
                raise TypeError()
            # Key may be any kind
            value = value[k] if k in value.keys() else value[eval(k)]
    except KeyError:
        print("Invalid Key", k)
        return None # Incase of key error returns None
    except TypeError:
        print("the object is not longer searchable")
        return None # If key is too long and object is no longer searchable
    return value


