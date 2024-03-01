N = int(input())
check = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if check[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            check[j] = False

length = len(primes)
count = start = end = 0
temp_sum = 0

while start <= end:
    if temp_sum >= N:
        if temp_sum == N:
            count += 1
        temp_sum -= primes[start]
        start += 1
    elif end == length:
        break
    else:
        temp_sum += primes[end]
        end += 1

print(count)
