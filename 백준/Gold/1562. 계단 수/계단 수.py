N = int(input())
dp = [[[0]*1024 for _ in range(10)] for __ in range(101)]
mod = 1000000000

for i in range(1, 10):
    dp[1][i][1<<i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(1024):
            if j == 0:
                dp[i][j][k|1<<j] = (dp[i][j][k|1<<j] + dp[i-1][j+1][k]) % mod
            elif j == 9:
                dp[i][j][k|1<<j] = (dp[i][j][k|1<<j] + dp[i-1][j-1][k]) % mod
            else:
                dp[i][j][k|1<<j] = (dp[i][j][k|1<<j] + dp[i-1][j-1][k] + dp[i-1][j+1][k]) % mod

print(sum([dp[N][i][1023] for i in range(10)]) % mod)
