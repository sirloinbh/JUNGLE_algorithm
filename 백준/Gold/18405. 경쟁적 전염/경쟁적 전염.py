import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


queue = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            queue.append((graph[i][j], i, j, 0))
queue.sort()
queue = deque(queue)


while queue:
    info, x, y, time = queue.popleft()
    if time == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not graph[nx][ny]:
            graph[nx][ny] = info
            queue.append((info, nx, ny, time + 1))

print(graph[X-1][Y-1])