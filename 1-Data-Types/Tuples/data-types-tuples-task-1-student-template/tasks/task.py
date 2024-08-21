from typing import Tuple


def get_tuple(num: int) -> Tuple[int]:
    num_str = str(num)
    return tuple(int(number) for number in num_str)

