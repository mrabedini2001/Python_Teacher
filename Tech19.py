#looping Techniques
#part1
ages = {'jack':20, 'mark':32, 'kevin':53, 'john':35}
for k, v in ages.items():
    print(k, v)
#part2
x = ['apple', 'lemon']
for i, j in enumerate(x):
    print(i, j)
#part3
names = ['jack', 'kevin']
ages = [23, 53]
for n, a in zip(names, ages):
    print(n, a)