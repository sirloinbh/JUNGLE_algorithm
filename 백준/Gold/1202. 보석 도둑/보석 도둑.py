import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewels = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jewels, [M, -V])

bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

value = 0
possible_jewels = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        M, V = heapq.heappop(jewels)
        heapq.heappush(possible_jewels, V)
    if possible_jewels:
        value -= heapq.heappop(possible_jewels)
    elif not jewels:
        break

print(value)
