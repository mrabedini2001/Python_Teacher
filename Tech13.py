#Functions 2
# b = [3, 4, 5]
def show(a, b=[]):
    b.append(a)
    return b

x = show(3)
x = show(4)
x = show(5)
print(x)