from collections import deque


class HistoryDict:
    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = dict()
        self.__changed_keys = deque()
        self.__dict = dictionary

    def set_value(self, key, value):
        if key not in self.__dict or self.__dict[key] != value:
            if len(self.__changed_keys) == 5:
                self.__changed_keys.popleft()
            self.__changed_keys.append(key)
        self.__dict[key] = value

    def get_history(self):
        return list(self.__changed_keys)
