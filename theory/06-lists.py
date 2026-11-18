# lists

numbers = [3, 1, 4, 1, 5, 9]
print(numbers)
print(numbers[0])    # first element
print(numbers[-1])   # last element
print(numbers[1:4])  # slicing

numbers.append(2)
print(numbers)

numbers.remove(1)  # removes the first 1
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(len(numbers))
print(5 in numbers)

# looping through a list
for n in numbers:
    print(n * 2)

# list comprehension - short way to build a list
squares = [n * n for n in range(1, 6)]
print(squares)

even = [n for n in range(10) if n % 2 == 0]
print(even)


# Sample output:
# [3, 1, 4, 1, 5, 9]
# 3
# 9
# [1, 4, 1]
# [3, 1, 4, 1, 5, 9, 2]
# [3, 4, 1, 5, 9, 2]
# [1, 2, 3, 4, 5, 9]
# [9, 5, 4, 3, 2, 1]
# 6
# True
# 18
# 10
# 8
# 6
# 4
# 2
# [1, 4, 9, 16, 25]
# [0, 2, 4, 6, 8]
