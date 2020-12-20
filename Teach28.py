# Scope
x = 10 # global scope
def show():
    global x
    print(x)
    x = 20 # local scope
    print(x)

show()
#print(x) in here dont work (is out of local)