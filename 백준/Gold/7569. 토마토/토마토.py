from collections import deque

# 입력: 박스의 크기
m, n, h = map(int, input().split())

# 3차원 리스트 초기화
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 방향 벡터 (상, 하, 좌, 우, 앞, 뒤)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# BFS 함수 정의
def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            # 범위 내에 있으며, 아직 안 익은 토마토라면
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomatoes[nx][ny][nz] == 0:
                # 토마토를 익게 하고, 큐에 추가
                tomatoes[nx][ny][nz] = tomatoes[x][y][z] + 1
                q.append((nx, ny, nz))

q = deque()
# 처음에 익은 토마토 위치 찾기
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 1:
                q.append((i, j, k))

# BFS 실행
bfs()

# 모든 토마토가 익었는지 확인하고, 익지 않은 토마토가 있다면 -1 출력
for i in tomatoes:
    for j in i:
        if 0 in j:
            print(-1)
            exit()

# 모든 토마토가 익은 경우 최대 시간 출력
days = max([max(i) for j in tomatoes for i in j]) - 1
print(days)