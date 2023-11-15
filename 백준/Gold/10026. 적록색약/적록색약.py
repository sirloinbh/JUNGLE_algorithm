import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 1,000,000으로 설정

# 입력: 그림의 크기
n = int(input())

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 탐색 함수 정의
def dfs(x, y, color, graph, visited):
    # 현재 위치를 방문 처리
    visited[x][y] = True
    # 4방향(상,하,좌,우)으로 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위 내에 있으며, 아직 방문하지 않았고, 같은 색상일 경우
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == color:
            dfs(nx, ny, color, graph, visited)

# 그래프(그림) 입력
graph = [list(input()) for _ in range(n)]
# 일반 사람과 적록색약인 사람을 위한 방문 정보 저장 리스트 초기화
visited_normal = [[False] * n for _ in range(n)]
visited_colorblind = [[False] * n for _ in range(n)]

# 일반 사람이 보는 구역의 수 구하기
count_normal = 0
for i in range(n):
    for j in range(n):
        # 아직 방문하지 않았다면
        if not visited_normal[i][j]:
            # DFS로 해당 구역을 탐색하고 구역 개수 1 증가
            dfs(i, j, graph[i][j], graph, visited_normal)
            count_normal += 1

# 적록색약인 사람을 위한 그래프 복사 및 수정
graph_colorblind = [row[:] for row in graph]
for i in range(n):
    for j in range(n):
        if graph_colorblind[i][j] == 'G':
            graph_colorblind[i][j] = 'R'  # 'G'를 'R'로 변경

# 적록색약인 사람이 보는 구역의 수 구하기
count_colorblind = 0
for i in range(n):
    for j in range(n):
        if not visited_colorblind[i][j]:
            dfs(i, j, graph_colorblind[i][j], graph_colorblind, visited_colorblind)
            count_colorblind += 1

# 결과 출력
print(count_normal, count_colorblind)