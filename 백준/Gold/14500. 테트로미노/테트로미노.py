n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 테트로미노를 탐색하기 위한 방향 벡터 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문 여부를 확인하기 위한 배열
visited = [[False] * m for _ in range(n)]

# 최대 합을 저장할 변수
result = 0

# DFS를 사용하여 테트로미노를 만드는 함수
def dfs(x, y, depth, total):
    global result
    if depth == 4:
        result = max(result, total)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, total+board[nx][ny])
            visited[nx][ny] = False

# 'ㅗ' 모양을 확인하는 함수
def check_exception(x, y):
    global result
    for i in range(4):
        temp = board[x][y]
        for j in range(3):
            t = (i+j) % 4
            nx, ny = x + dx[t], y + dy[t]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                temp = 0
                break
            temp += board[nx][ny]
        result = max(result, temp)

# 모든 위치에 대해 탐색 시작
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_exception(i, j)

print(result)
