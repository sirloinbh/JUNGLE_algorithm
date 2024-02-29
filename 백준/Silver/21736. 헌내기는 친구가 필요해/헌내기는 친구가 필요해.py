from collections import deque

# 상하좌우 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if campus[nx][ny] == 'O' or campus[nx][ny] == 'P':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    if campus[nx][ny] == 'P':
                        count += 1
    return count

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 헌내기 위치 찾기
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            x, y = i, j

friends = bfs(x, y)
if friends == 0:
    print('TT')
else:
    print(friends)
