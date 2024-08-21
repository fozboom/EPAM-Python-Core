from typing import Any, Dict, List, Set


def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    result = set()
    for dictionary in lst:
        for value in dictionary.values():
            result.add(value)
    return result
