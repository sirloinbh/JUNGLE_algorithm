n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 동적 프로그래밍 테이블 초기화
dp = [0] * (k+1)
dp[0] = 1  # 0원을 만드는 방법은 1가지

# 동전별로 동적 프로그래밍 진행
for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]

print(dp[k])