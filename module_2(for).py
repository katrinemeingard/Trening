numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    for y in range(2, i):
        if i % y == 0:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime:
        primes.append(i)
print(primes)
print(not_primes)
