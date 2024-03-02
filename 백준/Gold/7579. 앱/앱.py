import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

dp = [0 for _ in range(sum(C)+1)]
max_value = sum(C)

for i in range(1, N + 1):
    for j in range(max_value, C[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - C[i]] + A[i])

for i in range(max_value + 1):
    if dp[i] >= M:
        print(i)
        break
