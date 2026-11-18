# problem: find the largest of three numbers

a = 12
b = 45
c = 23

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("largest is", largest)

# shorter way
print("largest is", max(a, b, c))


# Sample output:
# largest is 45
# largest is 45
