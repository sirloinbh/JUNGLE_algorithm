from collections import deque

# 상, 하, 좌, 우 이동을 위한 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 섬에 번호를 할당하는 함수
def number_islands(x, y, number):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    graph[x][y] = number

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                graph[nx][ny] = number
                queue.append((nx, ny))

# 모든 섬에 대해 최단 거리를 구하는 함수
def shortest_bridge(number):
    dist = [[-1] * n for _ in range(n)]
    queue = deque()

    # 해당 섬의 모든 위치를 큐에 넣고 거리를 0으로 설정
    for i in range(n):
        for j in range(n):
            if graph[i][j] == number:
                queue.append((i, j))
                dist[i][j] = 0

    # BFS 수행
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 0 and graph[nx][ny] != number:
                    return dist[x][y]
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return float('inf')

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

number = 1

# 모든 섬에 번호를 할당
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            number_islands(i, j, number)
            number += 1

answer = float('inf')

# 모든 섬에 대해 최단 거리를 찾음
for i in range(1, number):
    answer = min(answer, shortest_bridge(i))

print(answer)