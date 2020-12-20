# Special, Magic Methods
class Car:
    def __init__(self, name, speed, price): # Dunder
        self.name = name
        self.speed = speed
        self.price = price

    def show(self):
        print(f'{self.name} cost {self.price} and top speed is {self.speed}')

  #  def __str__(self):
  #      return f'{self.name}-{self.price}'

  #  def __add__(self, other):
  #      return self.speed + other.speed  

    def __len__(self):
        return len(self.name)

c1 = Car('Benz', 200, '500$')
c2 = Car('Pride', 150, '100$')
#print(c1)
#print(c1 + c2)
print(len(c2))
print(str.__len__('how are you?'))