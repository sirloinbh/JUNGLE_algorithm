# 계단의 개수 입력
n = int(input())

# 각 계단의 점수 입력
stairs = [0] + [int(input()) for _ in range(n)]

# dp를 초기화합니다. dp[i]는 i번째 계단에서 얻을 수 있는 최대 점수를 의미합니다.
dp = [0] * (n+1)

# 첫 번째와 두 번째 계단은 시작점이므로 각 계단의 점수를 초기 값으로 설정합니다.
dp[1] = stairs[1]
if n > 1:  # 계단이 1개만 주어진 경우를 대비한 조건
    dp[2] = stairs[1] + stairs[2]

# 3번째 계단부터 n번째 계단까지 최대 점수를 계산합니다.
for i in range(3, n+1):
    # i번째 계단 직전의 계단을 밟는 경우와, 그 전 계단을 밟는 경우 중 최대 점수를 선택합니다.
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

# n번째 계단에서의 최대 점수를 출력합니다.
print(dp[n])