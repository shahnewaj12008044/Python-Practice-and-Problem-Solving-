# problem: find the second largest number in a list

numbers = [12, 45, 23, 67, 34, 67, 89, 10]

unique = sorted(set(numbers))
print("second largest is", unique[-2])

# without using set and sort
largest = second = -1
for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("second largest is", second)


# Sample output:
# second largest is 67
# second largest is 67
