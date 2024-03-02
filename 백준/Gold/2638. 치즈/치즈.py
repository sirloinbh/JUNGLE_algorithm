from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt(x, y):
    queue = deque([(x, y)])
    board[x][y] = -1  # 외부 공기를 -1로 표시
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = -1
                queue.append((nx, ny))

def count_time():
    time = 0
    while True:
        melt(0, 0)  # 외부 공기 탐색 및 표시
        melt_list = []
        for x in range(N):
            for y in range(M):
                if board[x][y] == 1:
                    air_count = 0
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if board[nx][ny] == -1:
                            air_count += 1
                    if air_count >= 2:
                        melt_list.append((x, y))
        if not melt_list:
            return time
        for x, y in melt_list:
            board[x][y] = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == -1:
                    board[i][j] = 0  # 외부 공기 초기화
        time += 1

print(count_time())
