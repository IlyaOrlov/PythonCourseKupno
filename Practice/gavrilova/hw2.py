class Tank:

    caption = ""
    speed = 0
    length = 0
    armament = ""

    def say_caption(self):
        print (f"Наименование танка {self.caption}")

    def say_length(self):
        print (f"Длина танка {self.length}")

    def say_speed(self):
        print (f"Подвижность танка {self.speed}")

    def say_armament(self):
        print (f"Вооружение танка {self.armament}")

t34 = Tank()
t34.caption = "Т34"
t34.length = 5964
t34.speed = 54
t34.armament = "76-мм танковая пушка ф-34"

tiger = Tank()
tiger.caption = "Tiger"
tiger.length = 8450
tiger.speed = 45
tiger.armament = "88-мм KwK 36"

t34.say_caption()
t34.say_length()
t34.say_speed()
t34.say_armament()


tiger.say_caption()
tiger.say_length()
tiger.say_speed()
tiger.say_armament()