import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
dp = [0]
trace = [0 for _ in range(N + 1)]

for i in range(N):
    if dp[-1] < sequence[i]:
        dp.append(sequence[i])
        trace[i] = len(dp) - 1
    else:
        idx = bisect_left(dp, sequence[i])
        dp[idx] = sequence[i]
        trace[i] = idx

i = len(dp) - 1
stack = []
for idx in range(N - 1, -1, -1):
    if trace[idx] == i:
        stack.append(sequence[idx])
        i -= 1

print(len(stack))
while stack:
    print(stack.pop(), end=' ')
