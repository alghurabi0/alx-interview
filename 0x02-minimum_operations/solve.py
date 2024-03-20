#!/usr/bin/python3
""" minimum operation solution """


def minOperations(n) -> int:
    if n <= 1:
        return 0
    #1-find prime factors
    #2-calculate initial operations requires for any of the primes (let's pick first) - should equal the prime
    #3-calculate the rest by performing selectAll once for each of the rest primes (except the last one) and Pase (prime values) times
    primes = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            primes.append(divisor)
            n //= divisor
        divisor += 1
    """print(primes)
    operations = primes[0]
    print(primes)
    i = 1
    while i < len(primes) - 1:
        operations += primes[i-1]
        i += 1
    operations += primes[len(primes)-2]"""
    total = 0
    for num in primes:
        total += num
    return total
