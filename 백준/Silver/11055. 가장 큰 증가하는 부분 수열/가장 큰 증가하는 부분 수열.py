# 입력
n = int(input())  # 수열의 길이 입력
arr = list(map(int, input().split()))  # 수열 입력

# dp 리스트 초기화. dp[i]는 i번째까지의 증가 부분 수열의 최대 합
dp = [x for x in arr]

# 동적 프로그래밍 수행
for i in range(n):
    for j in range(i):
        # arr[j] < arr[i]는 증가 부분 수열 조건을 확인하는 부분
        if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]

# 결과 출력: dp의 최댓값
print(max(dp))