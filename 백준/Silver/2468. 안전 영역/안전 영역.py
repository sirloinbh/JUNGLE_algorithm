N = int(input())  # 지역의 크기를 입력받습니다.
area = [list(map(int, input().split())) for _ in range(N)]  # 지역의 높이 정보를 2차원 배열로 입력받습니다.

# 네 방향(상, 하, 좌, 우)으로 이동하기 위한 리스트입니다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수 정의: 특정 지점부터 시작하여 상하좌우로 물의 높이보다 높은 지점을 탐색합니다.
def bfs(i, j, h, visited):
    queue = [(i, j)]  # 시작 지점을 큐에 추가합니다.
    visited[i][j] = True  # 시작 지점을 방문 처리합니다.

    while queue:  # 큐가 빌 때까지 반복합니다.
        x, y = queue.pop(0)  # 큐에서 지점을 하나 가져옵니다.
        
        # 현재 지점에서 네 방향으로 이동합니다.
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 다음 지점이 지역의 범위 내에 있으며, 아직 방문하지 않았고, 물의 높이보다 높다면
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and area[nx][ny] > h:
                visited[nx][ny] = True  # 해당 지점을 방문 처리합니다.
                queue.append((nx, ny))  # 해당 지점을 큐에 추가합니다.

answer = 1  # 최소 안전 영역 개수는 1입니다.

# 지역의 최소 높이와 최대 높이를 구합니다.
min_height = min(map(min, area))
max_height = max(map(max, area))

# 가능한 모든 물의 높이에 대해 안전 영역을 구합니다.
for h in range(min_height, max_height + 1): 
    visited = [[False] * N for _ in range(N)]  # 방문 정보를 초기화합니다.
    count = 0  # 해당 높이에서의 안전 영역 개수를 저장할 변수입니다.

    # 모든 지점에 대해 검사합니다.
    for i in range(N):
        for j in range(N):
            # 아직 방문하지 않았고, 물의 높이보다 높은 지점에서만 bfs를 시작합니다.
            if not visited[i][j] and area[i][j] > h:
                bfs(i, j, h, visited)
                count += 1  # 안전 영역 개수를 증가시킵니다.

    answer = max(answer, count)  # 최대 안전 영역 개수를 갱신합니다.

print(answer)  # 최대 안전 영역 개수를 출력합니다.