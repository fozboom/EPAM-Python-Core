from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    s = s.lower()
    result = {}
    for character in s:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result
