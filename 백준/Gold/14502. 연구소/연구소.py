from itertools import combinations
from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start, arr):
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx, ny))

def count_safe(arr):
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    return count

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
empty, virus = [], []
max_value = 0

for i in range(N):
    for j in range(M):
        if area[i][j] == 0:
            empty.append((i, j))
        elif area[i][j] == 2:
            virus.append((i, j))

for walls in combinations(empty, 3):
    temp = copy.deepcopy(area)
    for x, y in walls:
        temp[x][y] = 1
    for v in virus:
        bfs(v, temp)
    max_value = max(max_value, count_safe(temp))

print(max_value)
