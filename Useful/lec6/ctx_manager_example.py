import time


class MyCtxManager:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Total: {time.time() - self.start}")

