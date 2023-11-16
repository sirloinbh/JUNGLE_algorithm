from collections import deque

def bfs(grid, N, M):
    # 방문 배열: (벽을 부수고 온 경우, 부수지 않고 온 경우)
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0, 1, 0)])  # (x, y, 이동 거리, 벽 부수기 사용 여부)

    # BFS
    while queue:
        x, y, dist, wall = queue.popleft()

        # 도착 지점에 도달한 경우
        if x == N - 1 and y == M - 1:
            return dist

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아니고 아직 방문하지 않은 경우
                if grid[nx][ny] == 0 and not visited[nx][ny][wall]:
                    visited[nx][ny][wall] = True
                    queue.append((nx, ny, dist + 1, wall))
                # 벽이고 아직 벽을 부수지 않은 경우
                elif grid[nx][ny] == 1 and wall == 0:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, dist + 1, 1))

    # 도달할 수 없는 경우
    return -1

# 입력
N, M = map(int, input().split())
grid = [list(map(int, list(input().strip()))) for _ in range(N)]

# BFS 실행
print(bfs(grid, N, M))