R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - ord('A'), input().strip())) for _ in range(R)]

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited, count):
    global answer
    answer = max(answer, count)
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            # 현재 알파벳의 비트가 0이면 (방문하지 않았으면)
            if not visited & (1 << board[nx][ny]):
                dfs(nx, ny, visited | (1 << board[nx][ny]), count + 1)

answer = 0
dfs(0, 0, 1 << board[0][0], 1)
print(answer)
