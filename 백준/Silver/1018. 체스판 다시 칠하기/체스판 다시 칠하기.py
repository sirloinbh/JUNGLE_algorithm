N, M = map(int, input().split())

board1 =[['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W']]

board2 =[['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B']]

board = []
for _ in range(N) :
    board.append(list(input()))
minimum = 10000000000
for i in range(N-7) :
    for j in range(M -7) :
        new_board = [row[j:j+8] for row in board[i:i+8]]
        minimum = min(minimum,sum(a != b for row1, row2 in zip(new_board, board1) for a, b in zip(row1, row2)))
        minimum = min(minimum,sum(a != b for row1, row2 in zip(new_board, board2) for a, b in zip(row1, row2)))
        
print(minimum)