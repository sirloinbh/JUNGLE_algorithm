def DFS(N, row, columns, diagonals1, diagonals2):
    global result
    if row == N:
        result += 1
        return
    for col in range(N):
        if columns[col] and diagonals1[row - col] and diagonals2[row + col]:
            columns[col] = diagonals1[row - col] = diagonals2[row + col] = False
            DFS(N, row + 1, columns, diagonals1, diagonals2)
            columns[col] = diagonals1[row - col] = diagonals2[row + col] = True

N = int(input())
result = 0
columns = [True] * N
diagonals1 = [True] * (2 * N - 1)
diagonals2 = [True] * (2 * N - 1)
DFS(N, 0, columns, diagonals1, diagonals2)
print(result)
