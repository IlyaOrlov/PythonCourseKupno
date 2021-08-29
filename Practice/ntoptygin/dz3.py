# Спроектировать классы (один или несколько) для игры в танки и создать объекты этих классов.
class Tank:
    def print_info(self):
        print(f'Модель танка: {self.name}, максимальная скорость: {self.speed}, запас хода: {self.power_reserve}')


t34 = Tank()
t34.name = 'т34'
t34.power_reserve = '160'
t34.speed = '35'

t72 = Tank()
t72.name = 'т72'
t72.power_reserve = '700'
t72.speed = '50'

t90 = Tank()
t90.name = 'т90'
t90.power_reserve = '650'
t90.speed = '70'

x = input("Характеристики какого танка Вы хотите узнать? т34, т72 или т90? ")
if x == 'т34':
    t34.print_info()
if x == 'т72':
    t72.print_info()
if x == 'т90':
    t90.print_info()