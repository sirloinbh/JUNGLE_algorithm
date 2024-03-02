def is_valid(x, y, val):
    # 같은 행에 val이 있는지 확인
    for i in range(9):
        if board[x][i] == val:
            return False
    # 같은 열에 val이 있는지 확인
    for i in range(9):
        if board[i][y] == val:
            return False
    # 같은 3x3 박스에 val이 있는지 확인
    start_x, start_y = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if board[start_x + i][start_y + j] == val:
                return False
    return True

def solve_sudoku(depth):
    if depth == len(blanks):
        for row in board:
            print(''.join(map(str, row)))
        exit(0)  # 첫 번째 완성된 보드를 출력하고 프로그램 종료

    x, y = blanks[depth]
    for val in range(1, 10):
        if is_valid(x, y, val):
            board[x][y] = val
            solve_sudoku(depth + 1)
            board[x][y] = 0  # 백트래킹

board = [list(map(int, list(input().strip()))) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

solve_sudoku(0)
