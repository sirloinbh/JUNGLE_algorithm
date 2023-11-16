from collections import deque

# 상하좌우 이동을 위한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수 정의
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1  # 현재 연결된 영역의 칸 수

    while queue:
        x, y = queue.popleft()
        # 4방향으로의 이동 시도
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 새로운 위치가 유효하고, 아직 방문하지 않았으며, 빈 칸일 경우
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count

# 입력: 세로, 가로, 사각형의 개수
M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

# 사각형 그리기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

areas = []
# 보드의 모든 칸에 대하여
for i in range(M):
    for j in range(N):
        # 아직 방문하지 않은 빈 칸일 경우
        if board[i][j] == 0 and not visited[i][j]:
            areas.append(bfs(i, j))  # bfs 실행하고 반환된 영역의 크기를 areas에 추가

# 출력
areas.sort()
print(len(areas))
print(*areas)