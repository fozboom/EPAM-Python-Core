from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    unique_elements = set(str_list)
    result = list(unique_elements)
    result.sort()
    return result
