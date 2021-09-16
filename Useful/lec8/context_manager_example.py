class MyCtxManager:
    def __enter__(self):
        print("Hello")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Bye")


with MyCtxManager():
    print('Something')

with MyCtxManager():
    print('Something else')