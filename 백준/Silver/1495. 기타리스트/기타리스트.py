N, S, M = map(int, input().split())
V = list(map(int, input().split()))
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 0:
            continue
        if j + V[i] <= M:
            dp[i+1][j+V[i]] = 1
        if j - V[i] >= 0:
            dp[i+1][j-V[i]] = 1

result = -1
for i in range(M, -1, -1):
    if dp[N][i] == 1:
        result = i
        break

print(result)