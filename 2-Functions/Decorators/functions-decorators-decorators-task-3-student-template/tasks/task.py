def validate(function):
    def wrapper(x: int, y: int, z: int):
        for coordinate in (x, y, z):
            if coordinate < 0 or coordinate > 256:
                return "Function call is not valid!"
        return "Pixel created!"

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    pass
