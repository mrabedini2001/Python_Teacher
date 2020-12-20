# Methods => 1.Regular, 2.Class, 3.Static
import datetime

class Car:
    ###   Regular Methods   ###
    def __init__(self, name, speed, price, age):
        self.name = name
        self.speed = speed 
        self.price = price
        self.age = age

    def show(self):
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')
    ###   Class Methods   ###
    @classmethod # Decorator
    def from_birth(cls, name, speed, price, age):
        return cls(name, speed, price, datetime.datetime.now().year - age)
    ###   Static Methode   ###
    @staticmethod # Decorator
    def is_scrap(age):
        if age > 15:
            print('yes')
        else:
            print('no')

c1 = Car.from_birth('Pride', 150, '100$', 1995)
c2 = Car.from_birth('Benz', 300, '800$', 2012)

Car.is_scrap(18)
print(c2.age)