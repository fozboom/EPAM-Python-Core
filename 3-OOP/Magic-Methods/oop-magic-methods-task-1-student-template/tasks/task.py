from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, b):
        return [f"{word} {b}" for word in self.values]
