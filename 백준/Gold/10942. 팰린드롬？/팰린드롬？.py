import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if seq[i] == seq[i+1]:
        dp[i][i+1] = 1

for i in range(2, n):
    for j in range(n-i):
        if seq[j] == seq[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
