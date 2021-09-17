# Написать класс Man, который принимает имя в конструкторе.
# Имеет метод solve_task, который просто выводит "I'm not ready yet"

class Man:

    def __init__(self, name):
        self.name = name
    def solve_task(self):
        print(f"I'm {self.name} and i'm not ready yet")

# чтобы этот код не выполнялся в dz14 - прописываем вот это:
if __name__ == "__main__":
    a = Man('Ivan')
    a.solve_task()