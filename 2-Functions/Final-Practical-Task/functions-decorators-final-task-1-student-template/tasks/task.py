from typing import List


def find_end_pos(data: str, cur_pos, target: str, func_type: int):
    """
    Finds the end position of the target substring in the data string starting from cur_pos.

    Parameters:
    data (str): The string to search within.
    cur_pos (int): The current position to start searching from.
    target (str): The substring to search for.
    func_type (int): If 1, the function will continue to move cur_pos to the end of consecutive target substrings.

    Returns:
    int: The position of the end of the target substring. Returns -1 if the target is not found or if func_type is 1 and the end of the data string is reached.
    """
    if func_type:
        cur_pos = data.find(target, cur_pos)
        while cur_pos < len(data) - 1 and data[cur_pos + 1] == target:
            cur_pos += 1
        if cur_pos == len(data) - 1:
            return -1
    else:
        cur_pos = data.find(target, cur_pos)
    return cur_pos


def split(data: str, sep=None, maxsplit=-1):
    result = []
    start_pos, splits = 0, 0
    func_type = 1 if sep is None else 0

    if sep is None:
        sep = " "
        data = data.lstrip()

    while maxsplit == -1 or splits < maxsplit:
        end_pos = find_end_pos(data, start_pos, sep, func_type)
        if end_pos == -1:
            break
        result.append(data[start_pos:end_pos].strip() if func_type else data[start_pos:end_pos])
        start_pos = end_pos + len(sep)
        splits += 1
    to_add = data[start_pos:]
    if to_add or not func_type:
        result.append(to_add)

    return result


if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
