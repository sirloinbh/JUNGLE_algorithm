from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_sum = []
B_sum = defaultdict(int)

for i in range(n):
    _sum = 0
    for j in range(i, n):
        _sum += A[j]
        A_sum.append(_sum)

for i in range(m):
    _sum = 0
    for j in range(i, m):
        _sum += B[j]
        B_sum[_sum] += 1

A_sum.sort()
result = 0

for key in A_sum:
    result += B_sum[T - key]

print(result)
