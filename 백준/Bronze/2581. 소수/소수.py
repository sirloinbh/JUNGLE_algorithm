M = int(input())
N = int(input())
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for j in range(3, int(num**0.5) + 1, 2):
        if num % j == 0:
            return False
    return True

primes = [i for i in range(M,N+1) if is_prime(i)]
if primes :
    print(sum(primes))
    print(min(primes))
else :
    print(-1)