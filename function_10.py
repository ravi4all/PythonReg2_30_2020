# Nested Functions

def calc():
    x = 12
    y = 11

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    return add,sub

a,b = calc()
print(a())
print(b())