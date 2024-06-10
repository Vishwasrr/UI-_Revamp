def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


primes = list(filter(is_prime, range(2, 51)))
print(primes)

spaces = 4
for i in range(1, 6):
    print('*' * i + ' ' * spaces + '*' * i)
    spaces -= 1
