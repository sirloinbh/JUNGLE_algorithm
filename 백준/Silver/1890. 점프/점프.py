import sys

N = int(sys.stdin.readline().strip())

maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip().split())))

dp = []
for _ in range(N):
    dp.append([0] * N)


def search(maze, N, i, j):
    result = 0

    now_value = maze[i][j]
    if now_value == 0 and i == N - 1 and j == N - 1:
        return 1

    if now_value > 0 and i + now_value < N:
        if dp[i + now_value][j] > 0:
            result += dp[i + now_value][j]
            dp[i][j] = result
        else:
            result += search(maze, N, i + now_value, j)
            dp[i][j] = result

    if now_value > 0 and j + now_value < N:
        if dp[i][j + now_value] > 0:
            result += dp[i][j + now_value]
            dp[i][j] = result
        else:
            result += search(maze, N, i, j + now_value)
            dp[i][j] = result

    return result


print(search(maze, N, 0, 0))