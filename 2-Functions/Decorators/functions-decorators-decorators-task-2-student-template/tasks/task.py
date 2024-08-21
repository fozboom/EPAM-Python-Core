import inspect
import time


def log(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        param_names = inspect.signature(fn).parameters.keys()
        arg_names = list(param_names)[:len(args)]
        with open("log.txt", "w") as file:
            file.write(f"{fn.__name__}; ")
            args_str = ", ".join(f"{name}={value}" for name, value in zip(arg_names, args))
            kwargs_str = ", ".join(f"{key}={value}" for key, value in kwargs.items())
            file.write(f"args: {args_str}; kwargs: {kwargs_str}; ")
            file.write(f"execution time: {end_time - start_time} sec.")
        return result

    return wrapper
