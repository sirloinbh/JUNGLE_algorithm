from collections import deque

# 입력: 미로의 크기 N, M
N, M = map(int, input().split())

# 미로 정보 입력 받기
maze = [list(map(int, input().strip())) for _ in range(N)]

# 방문 표시 및 거리 정보 저장을 위한 리스트 초기화
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1  # 시작 지점 방문 표시

# 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 경계 내부이며, 갈 수 있는 길이고, 아직 방문하지 않은 경우
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                # 해당 위치를 큐에 넣기
                queue.append((nx, ny))
                # 방문 했음을 표시하며, 시작 위치로부터의 거리 정보 저장
                visited[nx][ny] = visited[x][y] + 1

bfs()

# 도착 지점까지의 최단 거리 출력
print(visited[N-1][M-1])