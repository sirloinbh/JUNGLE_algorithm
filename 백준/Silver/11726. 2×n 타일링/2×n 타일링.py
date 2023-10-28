# n 입력 받기
n = int(input())

# dp 리스트 초기화
dp = [0] * (n+1)

# 초기 조건 설정
dp[1] = 1
if n > 1:  # n이 1인 경우를 대비한 조건
    dp[2] = 2

# 3부터 n까지 dp 값을 채워 나갑니다.
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007  # 문제에서 요구한대로 10,007로 나눈 나머지를 저장

# 결과 출력
print(dp[n])