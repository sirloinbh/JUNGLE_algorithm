import sys
input = sys.stdin.readline
INF = float("inf")

def tsp(dp, visited, current):
    if visited == (1<<n) - 1:
        return w[current][0] or INF

    if dp[current][visited] is not None:
        return dp[current][visited]

    temp = INF
    for i, cost in enumerate(w[current]):
        if visited & (1 << i) == 0 and cost != 0:
            temp = min(temp, tsp(dp, visited | (1 << i), i) + cost)

    dp[current][visited] = temp
    return temp

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[None]*(1<<n) for _ in range(n)]
print(tsp(dp, 1, 0))
