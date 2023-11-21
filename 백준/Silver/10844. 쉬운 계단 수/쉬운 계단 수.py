N = int(input())

# dp 초기화
dp = [[0] * 10 for _ in range(N+1)]
for i in range(1, 10):  # 길이 1인 계단 수 초기화 (0으로 시작하는 수는 없으므로 제외)
    dp[1][i] = 1

# 동적 프로그래밍을 사용한 계단 수 계산
for i in range(2, N+1):
    for j in range(10):
        # j가 0일 때
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        # j가 9일 때
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        # 그 외의 경우
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# 길이 N인 계단 수의 총 개수를 1,000,000,000으로 나눈 나머지를 출력
print(sum(dp[N]) % 1_000_000_000)