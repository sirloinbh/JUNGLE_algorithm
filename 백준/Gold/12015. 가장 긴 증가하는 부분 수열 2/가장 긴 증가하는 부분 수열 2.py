import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
LIS = [0]

for i in range(N):
    if LIS[-1] < sequence[i]:
        LIS.append(sequence[i])
    else:
        LIS[bisect_left(LIS, sequence[i])] = sequence[i]

print(len(LIS)-1)
