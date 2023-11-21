N = int(input())

# DP 테이블 초기화
dp = [[0]*10 for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1

# DP를 통해 오르막 수의 개수 계산
for n in range(2, N+1):
    for i in range(10):
        dp[n][i] = sum(dp[n-1][:i+1])

# 결과 출력: N자리 모든 오르막 수의 합을 10007로 나눈 나머지
print(sum(dp[N]) % 10007)