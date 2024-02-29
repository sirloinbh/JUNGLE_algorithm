from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            x, y = i, j
            dist[i][j] = 0

BFS(x, y)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
