class PriceControl:
    def __init__(self):
        self.name = None

    def __get__(self, instance, value):
        return self.name

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            self.name = value
        else:
            raise ValueError


class NameControl:
    def __init__(self):
        self.name = None

    def __get__(self, instance, value):
        return self.name

    def __set__(self, instance, value):
        if self.name is not None:
            raise ValueError
        self.name = value


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.name = name
        self.price = price
        self.author = author
