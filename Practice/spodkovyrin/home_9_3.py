import pickle
import names
import random


class Human:

    def __init__(self, i, sex, name, surname, age, height):
        self.i = i
        self.sex = sex
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height

    def __repr__(self):
        return f'Human №{self.i}: Sex: "{self.sex}", Name: "{self.name} {self.surname}", Age: "{self.age}", ' \
               f'Height: "{self.height}"'


def generate_human(n):
    for i in range(n):
        dict = ['male', 'female']
        sex = random.choice(dict)
        if sex == 'male':
            name = names.get_first_name(gender=sex)
            surname = names.get_last_name()
        else:
            name = names.get_first_name(gender=sex)
            surname = names.get_last_name()
        age = random.randint(18, 65)
        height = random.randint(155, 196)
        human_i = Human(i, sex, name, surname, age, height)
        with open('human.data', 'ab') as f:
            pickle.dump(human_i, f)


def deser():
    with open('human.data', 'rb') as f:
        print(pickle.load(f))


generate_human(10)
deser()
