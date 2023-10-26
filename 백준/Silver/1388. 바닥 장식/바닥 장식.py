import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]


def dfs(x, y):
    visited[x][y] = True
    if graph[x][y] == '|':
        if x + 1 < n and graph[x + 1][y] == '|' and not visited[x + 1][y]:
            dfs(x + 1, y)
        return
    if graph[x][y] == '-':
        if y + 1 < m and graph[x][y + 1] == '-' and not visited[x][y + 1]:
            dfs(x, y + 1)
        return


count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)