# lambda, map, filter

# lambda is a small one-line function
square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(3, 4))

numbers = [1, 2, 3, 4, 5]

# map applies a function to every item
squared = list(map(lambda x: x * x, numbers))
print(squared)

# filter keeps only the items that pass the test
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# sorted with a key
students = [("Karim", 3.2), ("Rahim", 3.8), ("Shahnewaj", 3.5)]
students.sort(key=lambda s: s[1])
print(students)

# same thing written as a normal function, for comparison
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, numbers)))


# Sample output:
# 25
# 7
# [1, 4, 9, 16, 25]
# [2, 4]
# [('Karim', 3.2), ('Shahnewaj', 3.5), ('Rahim', 3.8)]
# [2, 4]
