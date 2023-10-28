T = int(input())
dp = [(1, 0), (0, 1)] + [(0, 0) for _ in range(100)]  # 100까지 확장

for i in range(2, 41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])

