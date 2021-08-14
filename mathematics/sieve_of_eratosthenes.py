from math import sqrt

def sieve_of_eratosthenes(n: int):
    if n <= 1:
        pass
    primes = [True for _ in range(n + 1)]
    proven_primes = []
    for i in range(2 , int(sqrt(n))):
        if primes[i]:
            j = i * i
            while j <= n:
                primes[j] = False
                j += i
    proven_primes.append(2)
    for i in range(3 , n + 1 , 2):
        if primes[i]:
            proven_primes.append(i)
    return proven_primes

if __name__ == '__main__':
    print( sieve_of_eratosthenes(900) )
