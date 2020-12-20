# Method (def in class)

# Part01
class Car:
    def __init__(self, name, speed, price):
        self.name = name 
        self.speed = speed
        self.price = price

    def show(self):
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')

c1 = Car('pride', 150, '100$')
c2 = Car('Benz', 300, '800$')

c1.show()
Car.show(c2)

# Part02
class main:
    def sayhello(self):
        print('Hello')

c1=main()
c1.sayhello()
main.sayhello(c1)