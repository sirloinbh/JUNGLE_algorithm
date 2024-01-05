import sys
sys.setrecursionlimit(10000)

def zet(N, r, c, row, col, cnt):
    if N == 0:
        return cnt

    size = 2 ** (N - 1)
    if r < row + size and c < col + size:
        return zet(N-1, r, c, row, col, cnt)
    elif r < row + size and c >= col + size:
        return zet(N-1, r, c, row, col + size, cnt + size * size)
    elif r >= row + size and c < col + size:
        return zet(N-1, r, c, row + size, col, cnt + 2 * size * size)
    else:
        return zet(N-1, r, c, row + size, col + size, cnt + 3 * size * size)



N, r, c= map(int,input().split())
print(zet(N, r, c, 0, 0, 0))