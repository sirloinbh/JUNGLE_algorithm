N = int(input())
A = list(map(int, input().split()))
def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    for j in range(3, int(num**0.5) + 1, 2):
        if num % j == 0:
            return False
    return True
primes = [i for i in A if is_prime(i)]
print(len(primes))