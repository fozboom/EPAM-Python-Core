from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    result = 0

    for item in sequence:
        if isinstance(item, (List, Tuple)):
            result += seq_sum(item)
        else:
            result += item
    return result
