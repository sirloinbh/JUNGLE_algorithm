from itertools import combinations

# 5x5 크기의 보드 입력 받기
board = [list(input()) for _ in range(5)]

# 상하좌우 이동을 위한 dx, dy 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 선택된 7개의 좌표가 서로 연결되어 있는지 BFS로 확인하는 함수
def bfs(points):
    # 방문 여부를 저장할 5x5 크기의 visited 리스트 초기화
    visited = [[0]*5 for _ in range(5)]
    
    # 시작점은 points의 첫 번째 좌표
    queue = [points[0]]
    visited[points[0][0]][points[0][1]] = 1
    
    # 연결된 학생의 수를 저장하는 cnt 변수
    cnt = 1

    while queue:
        x, y = queue.pop()
        for i in range(4):  # 상하좌우 방향 탐색
            nx, ny = x + dx[i], y + dy[i]
            # (nx, ny) 좌표가 points에 있고 아직 방문하지 않았다면
            if (nx, ny) in points and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문 표시
                queue.append((nx, ny))
                cnt += 1  # 연결된 학생 수 증가

    # 모든 학생이 연결되어 있다면 cnt는 7이 되어야 함
    return cnt == 7

# 5x5 격자판에서 7개의 좌표를 조합으로 선택
combi = combinations([(i, j) for i in range(5) for j in range(5)], 7)

# 조건을 만족하는 조합의 수를 저장할 answer 변수
answer = 0

for points in combi:
    # S의 개수가 4 이상인 경우만 검사
    if sum(1 for x, y in points if board[x][y] == 'S') >= 4:
        # bfs 함수를 사용하여 학생들이 서로 연결되어 있는지 확인
        if bfs(points):
            answer += 1  # 연결되어 있다면 답의 수 증가

# 조건을 만족하는 조합의 수 출력
print(answer)