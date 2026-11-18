# problem: factorial of a number
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print("factorial of", n, "is", fact)


# Sample output:
# factorial of 5 is 120
