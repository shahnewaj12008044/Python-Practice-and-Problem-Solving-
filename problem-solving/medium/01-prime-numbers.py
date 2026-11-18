# problem: check if a number is prime, and list primes up to 50

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))
print(is_prime(30))

primes = [n for n in range(2, 51) if is_prime(n)]
print(primes)


# Sample output:
# True
# False
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
