from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    try:
        a, b = map(int, str_with_ints.split())
        c = a / b
        return c
    except ZeroDivisionError:
        return "Error code: division by zero"

    except Exception as e:
        return f"Error code: {e}"

