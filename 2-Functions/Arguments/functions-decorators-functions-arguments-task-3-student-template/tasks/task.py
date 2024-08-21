from typing import Dict

def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    result = {}
    for dictionary in args:
        for key, value in dictionary.items():
            result[key] = result.get(key, 0) + value
    return result