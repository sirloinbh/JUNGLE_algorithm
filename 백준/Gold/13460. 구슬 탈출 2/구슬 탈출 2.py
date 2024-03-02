from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # up, down, left, right

def move(i, j, dx, dy):
    c = 0  # move count
    while board[i+dx][j+dy] != '#' and board[i][j] != 'O':
        i += dx
        j += dy
        c += 1
    return i, j, c

def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])  # red ball
            nbx, nby, bc = move(bx, by, dx[i], dy[i])  # blue ball
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    print(d)
                    return
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if [nrx, nry, nbx, nby] not in visited:
                    visited.append([nrx, nry, nbx, nby])
                    q.append([nrx, nry, nbx, nby, d+1])
    print(-1)

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited, q = [], deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j  # red ball
        if board[i][j] == 'B':
            bx, by = i, j  # blue ball
q.append([rx, ry, bx, by, 1])
visited.append([rx, ry, bx, by])

bfs()
