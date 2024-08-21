from typing import List


def check(row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    result = []

    for i in range(row_start, row_end + 1):
        current_row = []
        for j in range(column_start, column_end + 1):
            current_row.append(i * j)
        result.append(current_row)

    return result

