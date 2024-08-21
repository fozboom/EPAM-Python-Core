import os
import shutil
import string
import random


class TempDir:
    def __enter__(self):
        self.original_dir = os.getcwd()
        self.temp_dir = TempDir.create_temp_dir()
        os.chdir(self.temp_dir)
        return self.temp_dir

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_dir)
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    @staticmethod
    def create_temp_dir(name_length=8):
        characters = string.ascii_letters + string.digits
        while True:
            random_name = ''.join(random.choice(characters) for _ in range(name_length))
            random_path = os.path.join(os.getcwd(), random_name)
            if not os.path.exists(random_path):
                os.mkdir(random_path)
                return os.path.abspath(random_path)
