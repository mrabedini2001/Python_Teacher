# Inheritance => class Motor(Car)
class Car:
    wheels = 4
    def __init__(self, name, speed, price):
        self.name = name  # Atribute
        self.speed = speed # Atribute
        self.price = price # Atribute

    def show(self): # Method
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')

class Motor(Car):
    wheels = 2

    def __init__(self, name, speed, price, helmet): # Method
        super().__init__(name, speed, price)
        self.helmet = helmet

    def show(self): # Method
        super().show()
        print(f'hello, we are riding {self.name}.')

m1 = Motor('honda', 200, '500$', 'hat')
m1.show()
#help(m1) # method resolution order!