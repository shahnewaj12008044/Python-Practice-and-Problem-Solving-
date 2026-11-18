# variables and data types

name = "Shahnewaj"
age = 21
cgpa = 3.52
is_student = True

print(name, type(name))
print(age, type(age))
print(cgpa, type(cgpa))
print(is_student, type(is_student))

# python figures out the type by itself, no need to declare it
x = 10
print(x, type(x))
x = "now I am a string"
print(x, type(x))

# multiple assignment in one line
a, b, c = 1, 2, 3
print(a, b, c)

# swapping two numbers without a third variable
a, b = b, a
print(a, b)

# type conversion
num_str = "25"
num = int(num_str)
print(num + 5)

price = 99.5
print(int(price))  # float to int cuts off the decimal part


# Sample output:
# Shahnewaj <class 'str'>
# 21 <class 'int'>
# 3.52 <class 'float'>
# True <class 'bool'>
# 10 <class 'int'>
# now I am a string <class 'str'>
# 1 2 3
# 2 1
# 30
# 99
