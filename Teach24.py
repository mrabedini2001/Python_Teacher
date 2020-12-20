# Format

# Part01
name = 'Jack'
age = 24
print('{n} is {a} years old.'.format(a=age, n=name))

# Part02
info = {'Jack':20, 'mark':30}
info2 = {'jane':40, 'anna':50}
print('{0[Jack]} is {0[mark]} years old. {1[jane]} {1[anna]}'.format(info, info2))