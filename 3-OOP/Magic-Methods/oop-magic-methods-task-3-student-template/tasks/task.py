from __future__ import annotations

from abc import abstractmethod
from typing import Type


class Currency:
    conversions = {
        'Euro': {'Dollar': 2.0, 'Pound': 100.0},
        'Dollar': {'Euro': 0.5, 'Pound': 50.0},
        'Pound': {'Euro': 0.01, 'Dollar': 0.02}
    }

    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    @classmethod
    def short_form(cls) -> str:
        pass

    def __str__(self):
        return f"{float(self.value)} {self.__class__.short_form()}"

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        if cls == other_cls:
            return f"1.0 {cls.short_form()} for 1 {cls.short_form()}"
        result = cls.conversions[cls.__name__][other_cls.__name__]
        return f"{result} {other_cls.short_form()} for 1 {cls.short_form()}"

    def to_currency(self, other_cls: Type[Currency]):
        if self.__class__ == other_cls:
            return other_cls(self.value)
        rate = self.conversions[self.__class__.__name__][other_cls.__name__]
        return other_cls(float(self.value * rate))

    def __add__(self, other: Currency):
        to_plus = other.to_currency(self.__class__)
        return self.__class__(self.value + to_plus.value)

    def __lt__(self, other):
        other_in_self = other.to_currency(self.__class__)
        return self.value < other_in_self.value

    def __gt__(self, other):
        other_in_self = other.to_currency(self.__class__)
        return self.value > other_in_self.value

    def __eq__(self, other):
        other_in_self = other.to_currency(self.__class__)
        return self.value == other_in_self.value


class Euro(Currency):
    @classmethod
    def short_form(cls) -> str:
        return "EUR"


class Dollar(Currency):
    @classmethod
    def short_form(cls) -> str:
        return "USD"


class Pound(Currency):
    @classmethod
    def short_form(cls) -> str:
        return "GBP"
