import os


class Cd:
    def __init__(self, new_path):
        if not os.path.isdir(new_path):
            raise ValueError(f"The path {new_path} is not a valid directory.")
        self.new_path = new_path
        self.old_path = None

    def __enter__(self):
        self.old_path = os.getcwd()
        os.chdir(self.new_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.old_path)


# Пример использования
try:
    with Cd('/home'):
        print("Current directory:", os.getcwd())
except ValueError as e:
    print(e)

