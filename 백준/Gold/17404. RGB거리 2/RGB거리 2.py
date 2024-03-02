import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input())
cost = [[0]*3 for _ in range(N+1)]
dp = [[0]*3 for _ in range(N+1)]
for i in range(1, N+1):
    r, g, b = map(int, input().split())
    cost[i][0] = r
    cost[i][1] = g
    cost[i][2] = b

answer = INF
for first in range(3):  # 첫번째 집의 색상을 결정
    for color in range(3):
        if first == color:
            dp[1][color] = cost[1][color]
        else:
            dp[1][color] = INF

    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

    for color in range(3):
        if color == first:
            continue
        answer = min(answer, dp[N][color])

print(answer)
