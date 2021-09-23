import pickle
import names
import random


class Human:
    # human = []

    def __init__(self, i, sex, name, surname, age, height):
        self.i = i
        self.sex = sex
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        # Human.human.append(self)

    def __repr__(self):
        return f'Human № {self.i + 1}: Sex: "{self.sex}", Name: "{self.name} {self.surname}", Age: "{self.age}", ' \
               f'Height: "{self.height}"'


def generate_human(n):
    humans = []
    for i in range(n):
        lst = ['male', 'female']
        sex = random.choice(lst)
        if sex == 'male':
            name = names.get_first_name(gender=sex)
            surname = names.get_last_name()
        else:
            name = names.get_first_name(gender=sex)
            surname = names.get_last_name()
        age = random.randint(18, 65)
        height = random.randint(155, 196)
        human = Human(i, sex, name, surname, age, height)
        humans.append(human)
    return humans


def ser():
    with open('human.data', 'ab') as f:
        pickle.dump(generate_human(10), f)


def deser():
    with open('human.data', 'rb') as f:
        print(pickle.load(f))


# generate_human(10)
ser()
deser()
