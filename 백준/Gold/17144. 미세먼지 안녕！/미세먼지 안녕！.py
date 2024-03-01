import sys

r, c, t = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 상, 우, 하, 좌
cleaner = [i for i in range(r) if board[i][0] == -1]

def spread():
    tmp_board = [[0]*c for _ in range(r)]
    
    for x in range(r):
        for y in range(c):
            if board[x][y] >= 5:
                spread_amount = board[x][y]//5
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        tmp_board[nx][ny] += spread_amount
                        board[x][y] -= spread_amount
    for x in range(r):
        for y in range(c):
            board[x][y] += tmp_board[x][y]

def clean():
    # 위쪽 공기청정기
    for i in range(cleaner[0]-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(c-1):
        board[0][i] = board[0][i+1]
    for i in range(cleaner[0]):
        board[i][c-1] = board[i+1][c-1]
    for i in range(c-1, 1, -1):
        board[cleaner[0]][i] = board[cleaner[0]][i-1]
    board[cleaner[0]][1] = 0
    
    # 아래쪽 공기청정기
    for i in range(cleaner[1]+1, r-1):
        board[i][0] = board[i+1][0]
    for i in range(c-1):
        board[r-1][i] = board[r-1][i+1]
    for i in range(r-1, cleaner[1], -1):
        board[i][c-1] = board[i-1][c-1]
    for i in range(c-1, 1, -1):
        board[cleaner[1]][i] = board[cleaner[1]][i-1]
    board[cleaner[1]][1] = 0

for _ in range(t):
    spread()
    clean()

answer = sum(map(sum, board)) + 2
print(answer)
