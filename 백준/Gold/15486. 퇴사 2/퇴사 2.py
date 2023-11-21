import sys

def solve_retirement_faster(N, T, P):
    dp = [0] * (N + 2)
    max_profit = 0
    for i in range(1, N + 1):
        # 오늘까지의 최대 수익을 갱신
        max_profit = max(max_profit, dp[i])

        # 상담이 끝나는 날짜
        next_day = i + T[i - 1]

        # 상담 가능한 경우에만 수익 갱신
        if next_day <= N + 1:
            dp[next_day] = max(dp[next_day], max_profit + P[i - 1])

    return max(dp)

# 입력 처리 (sys.stdin.readline 사용)
N = int(sys.stdin.readline().strip())
T, P = [], []
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

# 결과 출력
print(solve_retirement_faster(N, T, P))
