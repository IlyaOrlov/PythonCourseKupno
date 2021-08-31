class Tank:
    power = 10
    speed = 5

    def __repr__(self):
        return "Tank"


class T34:
    power = 20
    speed = 20

    def __repr__(self):
        return "T34"


class Tiger:
    power = 30
    speed = 10

    def __repr__(self):
        return "Tiger"


lst = [T34(), Tank(), Tiger()]
lst.sort(key=lambda x: x.power)
print(lst)
