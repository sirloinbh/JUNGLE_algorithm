import sys
input = sys.stdin.readline

n = 10
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
INF = sys.maxsize
grid = [list(input().strip()) for _ in range(n)]
ans = INF

def count_on(grid):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'O':
                cnt += 1
    return cnt

def switch(x, y, grid):
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == '#':
                grid[nx][ny] = 'O'
            else:
                grid[nx][ny] = '#'

def solve():
    global ans
    for bit in range(1 << n):
        b = [list(row) for row in grid]
        cnt = 0
        for i in range(n):
            if bit & (1 << i):
                switch(0, i, b)
                cnt += 1
        for i in range(1, n):
            for j in range(n):
                if b[i-1][j] == 'O':
                    switch(i, j, b)
                    cnt += 1
        if count_on(b) == 0:
            ans = min(ans, cnt)

solve()
print(ans if ans != INF else -1)
