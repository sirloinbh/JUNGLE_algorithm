import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    graph[x][y] = 0
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    temp = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
                graph[nx][ny] = 0
                visited[nx][ny] = 1
                queue.append((nx, ny))
                temp += 1

    return temp


result = 0
answer = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            result += 1
            answer.append(bfs(i, j))

print(result)
answer.sort()
for a in answer:
    print(a)