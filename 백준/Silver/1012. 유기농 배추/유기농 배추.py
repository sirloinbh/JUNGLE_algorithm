from collections import deque

def bfs(graph, x, y):
    # 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0  # 방문한 배추 위치를 0으로 변경

    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우 네 방향에 대해 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0  # 방문한 배추 위치를 0으로 변경

# 테스트 케이스의 개수 입력
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())  # M: 가로 길이, N: 세로 길이, K: 배추 위치의 개수
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1  # 배추 위치를 1로 표시

    count = 0  # 필요한 배추흰지렁이 개수
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                count += 1  # 연결된 배추 그룹 발견 시 카운트 증가

    print(count)  # 결과 출력