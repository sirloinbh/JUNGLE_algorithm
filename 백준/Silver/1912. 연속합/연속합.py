# 입력
n = int(input()) # 수열의 길이 입력
arr = list(map(int, input().split())) # 수열 입력

# dp 리스트 초기화. dp[i]는 i번째까지의 최대 연속합
dp = [0] * n
dp[0] = arr[0]

# 동적 프로그래밍 수행
for i in range(1, n):
    # 이전까지의 연속합과 현재 값을 더한 값과 현재 값 중 큰 값을 dp[i]에 저장
    dp[i] = max(dp[i-1] + arr[i], arr[i])

# 결과 출력: dp의 최댓값
print(max(dp))