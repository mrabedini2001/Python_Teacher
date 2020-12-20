# Work with files

# part01
f = open('Hello.txt', 'w')
f.write("Hello World")

# part02
with open('Hello.txt') as f:
    data = f.read()
print(data)