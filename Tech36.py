# Porperty Decorator
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return f'{self.first} {self.last}'

    @property # Property Decorator
    def email(self):
        return f'{self.first}_{self.last}@email.com'

p = Person('amir', 'abed')
p.first = 'Jack'

print(p.first)
print(p.last)
print(p.email) # in here you dont need (()) for methods with @property Decorator
print(p.fullname())