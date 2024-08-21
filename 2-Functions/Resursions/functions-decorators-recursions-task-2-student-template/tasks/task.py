from typing import Any, List, Tuple


def linear_seq(sequence: List[Any]) -> List[Any]:
    result = []
    for item in sequence:
        if isinstance(item, (List, Tuple)):
            result += linear_seq(item)
        else:
            result += [item]
    return result
