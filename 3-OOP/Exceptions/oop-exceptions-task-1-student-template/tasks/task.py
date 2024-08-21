from math import ceil


class Pagination:
    def __init__(self, data: str, items_on_page: int):
        self.__text = data
        self.__item_count = len(data)
        self.__page_size = items_on_page
        self.__pages = [self.__text[i: i + self.__page_size] for i in range(0, len(data), self.__page_size)]
        self.__page_count = ceil(len(data) / items_on_page)

    @property
    def page_count(self):
        return self.__page_count

    @property
    def item_count(self):
        return self.__item_count

    def count_items_on_page(self, page_number):
        if page_number < 0 or page_number >= self.__page_count:
            raise Exception("Invalid index. Page is missing")
        return len(self.__pages[page_number])

    def find_page(self, data):
        page_numbers = []

        for i, page_data in enumerate(self.__pages):
            founded = False
            if data in page_data:
                page_numbers.append(i)
                founded = True
            if i < self.__page_count - 1:
                row = self.__pages[i] + self.__pages[i + 1]
                if data in row and not founded and data not in self.__pages[i + 1]:
                    page_numbers.extend([i, i + 1])

        if not page_numbers:
            raise Exception(f"'{data}' is missing on the pages")
        return sorted(set(page_numbers))

    def display_page(self, page_number):
        if page_number < 0 or page_number >= self.__page_count:
            raise Exception("Invalid index. Page is missing")
        return self.__pages[page_number]
