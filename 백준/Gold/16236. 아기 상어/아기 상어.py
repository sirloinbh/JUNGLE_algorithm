from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, size):
    q, visited = [(0, x, y)], set([(x, y)])

    while q:
        d, x, y = heappop(q)
        if 0 < space[x][y] < size:
            space[x][y] = 0
            return x, y, d
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
                if space[nx][ny] <= size:
                    visited.add((nx, ny))
                    heappush(q, (d+1, nx, ny))
    return -1, -1, -1

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
x, y, size, count, time = 0, 0, 2, 0, 0

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 0
            x, y = i, j

while True:
    nx, ny, d = bfs(x, y, size)
    if nx == -1:
        break
    x, y, time = nx, ny, time + d
    count += 1
    if size == count:
        size += 1
        count = 0

print(time)
