# problem: print the first n numbers of the fibonacci series
# 0, 1, 1, 2, 3, 5, 8, ...

n = 10
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# Sample output:
# 0 1 1 2 3 5 8 13 21 34 
