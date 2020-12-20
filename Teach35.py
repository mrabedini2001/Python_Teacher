# Access Point => Public, Protected, Private
class Person:
    name = 'amir' # Public
    _age = 32 # Protected
    __height = 180 # Private

class Male(Person):
    def show(self):
        print(self.__height)

p1 = Person()
print(p1._Person__height) #  Name Mangling  