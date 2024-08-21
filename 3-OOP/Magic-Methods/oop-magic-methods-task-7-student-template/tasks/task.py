import datetime
from contextlib import ContextDecorator


class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.datetime.now()
        run_time = end_time - self.start_time
        error_message = str(exc_val) if exc_val else "None"
        log_message = f"Start: {self.start_time} | Run: {run_time} | An error occurred: {error_message}\n"
        with open(self.filename, 'a') as log_file:
            log_file.write(log_message)
        if exc_type:
            return False
