# functions

def greet():
    print("Hello!")

greet()

def greet_person(name):
    print("Hello,", name)

greet_person("Shahnewaj")

def add(a, b):
    return a + b

print(add(5, 3))

# default argument
def power(base, exp=2):
    return base ** exp

print(power(4))
print(power(4, 3))

# *args - when you do not know how many arguments will come
def total(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(total(1, 2, 3))
print(total(10, 20))

# local vs global
x = 100

def show():
    x = 5  # this x is local, it does not touch the outer one
    print(x)

show()
print(x)

# recursion - factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# Sample output:
# Hello!
# Hello, Shahnewaj
# 8
# 16
# 64
# 6
# 30
# 5
# 100
# 120
