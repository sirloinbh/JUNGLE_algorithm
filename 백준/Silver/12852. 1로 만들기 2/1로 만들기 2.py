n = int(input())

# dp 배열 초기화
dp = [(0, []) for _ in range(n+1)]
dp[1] = (0, [1])

# 2부터 n까지 최소 연산 횟수와 연산 과정을 dp에 저장합니다.
for i in range(2, n+1):
    dp[i] = (dp[i-1][0] + 1, dp[i-1][1] + [i])

    if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0]:
        dp[i] = (dp[i//2][0] + 1, dp[i//2][1] + [i])

    if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0]:
        dp[i] = (dp[i//3][0] + 1, dp[i//3][1] + [i])

# 결과 출력
print(dp[n][0])
print(' '.join(map(str, reversed(dp[n][1]))))