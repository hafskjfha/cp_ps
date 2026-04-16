import math

def sieve_of_eratosthenes(M, N):

    is_prime = [True] * (N + 1)

    is_prime[0] = is_prime[1] = False

    

    for i in range(2, int(math.sqrt(N)) + 1):

        if is_prime[i]:

            for j in range(i * 2, N + 1, i):

                is_prime[j] = False

    

    primes = [i for i in range(M, N + 1) if is_prime[i]]

    return primes

M, N = map(int, input().split())

primes = sieve_of_eratosthenes(M, N)

for prime in primes:

    print(prime)

