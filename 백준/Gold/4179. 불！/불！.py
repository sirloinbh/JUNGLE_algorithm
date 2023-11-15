from collections import deque

def bfs(maze, R, C, fire_queue, jihun_queue):
    # 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while jihun_queue:
        # 불 확산
        for _ in range(len(fire_queue)):
            fx, fy = fire_queue.popleft()
            for i in range(4):
                nfx, nfy = fx + dx[i], fy + dy[i]
                if 0 <= nfx < R and 0 <= nfy < C and maze[nfx][nfy] == '.':
                    maze[nfx][nfy] = 'F'
                    fire_queue.append((nfx, nfy))

        # 지훈 이동
        for _ in range(len(jihun_queue)):
            x, y, time = jihun_queue.popleft()
            # 탈출 조건
            if x == 0 or x == R-1 or y == 0 or y == C-1:
                return time + 1  # 탈출 성공, 이동 시간 반환

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if maze[nx][ny] == '.':
                        jihun_queue.append((nx, ny, time + 1))
                        maze[nx][ny] = '#'  # 방문한 곳은 벽으로 처리

    return "IMPOSSIBLE"  # 탈출 불가능한 경우

# 입력 받기
R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

fire_queue = deque()
jihun_queue = deque()

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            fire_queue.append((i, j))
        elif maze[i][j] == 'J':
            jihun_queue.append((i, j, 0))  # 지훈의 위치와 시간 초기화

# BFS 실행
result = bfs(maze, R, C, fire_queue, jihun_queue)
print(result)