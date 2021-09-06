class Tank:
    power = 20
    speed = 10
    x = 0
    name = "Tank"

    def show(self):
        print(f"Tank {self.name} at {self.x}")

    def move(self):
        self.x += 1

    def shoot(self):
        print("Ba-bah")


class T34(Tank):
    power = 30
    speed = 50
    name = "T34"


class Tiger(Tank):
    power = 50
    speed = 20
    name = "Tiger"

    def shoot(self):
        print("Ba-ba-bah")


tanks = [Tank(), T34(), Tiger()]
while True:
    i = int(input("Select tank (0, 1, 2): "))
    if i > 2:
        break

    tanks[i].show()
    tanks[i].move()
    tanks[i].shoot()
    tanks[i].show()
