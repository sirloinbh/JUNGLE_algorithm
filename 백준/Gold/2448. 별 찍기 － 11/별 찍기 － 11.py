def draw_star(n, x, y):
    if n == 3:
        board[y][x] = '*'
        board[y+1][x-1] = board[y+1][x+1] = '*'
        board[y+2][x-2:x+3] = ['*']*5
        return

    div = n//2
    draw_star(div, x, y)
    draw_star(div, x-div, y+div)
    draw_star(div, x+div, y+div)

N = int(input())
board = [[' ']*2*N for _ in range(N)]
draw_star(N, N-1, 0)

for row in board:
    print(''.join(row))
