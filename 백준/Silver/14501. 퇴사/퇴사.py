# 입력: 첫 줄에 전체 상담 개수 N이 주어짐
N = int(input())

# 상담 정보를 입력받아 저장
T = []  # 상담을 완료하는데 걸리는 시간
P = []  # 상담을 했을 때 받을 수 있는 금액
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# dp[i]는 i일에 일을 시작했을 때 얻을 수 있는 최대 이익
dp = [0] * (N + 1)  # N+1일차까지 고려

# 마지막 날부터 첫 번째 날까지 역순으로 계산
for i in range(N-1, -1, -1):
    # i일에 상담을 했을 때 N일 안에 끝낼 수 있는 경우
    if i + T[i] <= N:
        dp[i] = max(dp[i + T[i]] + P[i], dp[i + 1])
    # 상담을 할 수 없는 경우(시간 초과)
    else:
        dp[i] = dp[i + 1]

# 결과 출력: 0일에 일을 시작했을 때 얻을 수 있는 최대 이익
print(dp[0])