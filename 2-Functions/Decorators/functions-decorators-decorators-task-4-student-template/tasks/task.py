def decorator_apply(lambda_func):
    def decorator_function(func):
        def wrapper(num: int):
            original_result = func(num)
            return lambda_func(original_result)

        return wrapper

    return decorator_function


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num
