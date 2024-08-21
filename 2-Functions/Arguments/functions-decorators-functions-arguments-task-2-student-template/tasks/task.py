def union(*args) -> set:
    result = set(args[0])
    for i in range(1, len(args)):
        result |= set(args[i])
    return result


def intersect(*args) -> set:
    result = set(args[0])
    for i in range(1, len(args)):
        result &= set(args[i])
    return result


print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))
print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))
