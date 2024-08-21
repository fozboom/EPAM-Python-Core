from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    result = []
    for i in range(len(lst) - 1):
        result.append((lst[i], lst[i + 1]))
    return result
