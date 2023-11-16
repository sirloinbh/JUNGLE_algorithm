from collections import deque

# 이동 방향 (상, 하, 좌, 우, 위, 아래)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(L, R, C, building, start):
    queue = deque([(*start, 0)]) # (z, x, y, 시간)
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

    while queue:
        z, x, y, time = queue.popleft()
        if building[z][x][y] == 'E':
            return time

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if building[nz][nx][ny] != '#' and not visited[nz][nx][ny]:
                    visited[nz][nx][ny] = True
                    queue.append((nz, nx, ny, time + 1))

    return "Trapped!"

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    start = None
    for z in range(L):
        floor = [list(input().strip()) for _ in range(R)]
        building.append(floor)
        input() # 공백 라인
        for x in range(R):
            for y in range(C):
                if floor[x][y] == 'S':
                    start = (z, x, y)

    result = bfs(L, R, C, building, start)
    print(f"Escaped in {result} minute(s)." if isinstance(result, int) else result)