# error handling

# division by zero
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("you cannot divide by zero")

# wrong type
try:
    num = int("abc")
except ValueError:
    print("that is not a number")

# file that does not exist
try:
    f = open("missing.txt", "r")
except FileNotFoundError:
    print("file not found")

# else runs when there is no error, finally always runs
try:
    x = 10 / 2
except ZeroDivisionError:
    print("error")
else:
    print("no error, result is", x)
finally:
    print("this always runs")

# raising your own error
try:
    age = 15
    if age < 18:
        raise ValueError("age must be 18 or above")
except ValueError as e:
    print("caught:", e)


# Sample output:
# you cannot divide by zero
# that is not a number
# file not found
# no error, result is 5.0
# this always runs
# caught: age must be 18 or above
