# Class Variables
class Car:
    wheel = 4 # class variables
    def __init__(self, name, speed, price):
        self.name = name # instance variables
        self.speed = speed # instance variables
        self.price = price # instance variables
    
    def show(self):
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')

    def show_wheels(self):
        print(f'{self.name} has {self.wheel} wheels')

c1 = Car('Price', 150, '100$')
c2 = Car('Benz', 300, '800$')

c1.wheel = 5 

#c1.show_wheels()
print(c2.__dict__)