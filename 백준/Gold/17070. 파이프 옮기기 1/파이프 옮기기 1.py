N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for __ in range(N)]
dp[0][1][0] = 1

for i in range(2, N):
    if house[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(1, N):
    for j in range(2, N):
        if house[i][j] or house[i-1][j] or house[i][j-1]:
            continue
        dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

    for j in range(1, N):
        if house[i][j]:
            continue
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

print(sum(dp[N-1][N-1]))
