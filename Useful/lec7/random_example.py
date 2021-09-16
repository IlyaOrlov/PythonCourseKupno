import random


def mychoice(data):
    i = random.randint(0, len(data))
    return data[i]


lst = ['Ivan', 'Petr', 'Fedor', 'Ilya']
name = random.choice(lst)
# print(name)

random.shuffle(lst)
print(lst)
