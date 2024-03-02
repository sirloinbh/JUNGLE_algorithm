from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, cnt):
    q = deque()
    q.append([x, y])
    c[x][y] = cnt
    num = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0 and c[nx][ny] == -1:
                q.append([nx, ny])
                c[nx][ny] = cnt
                num += 1
    return num

n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
c = [[-1]*m for _ in range(n)]
cnt = 0
group_num = [0]
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and c[i][j] == -1:
            cnt += 1
            group_num.append(bfs(i, j, cnt))

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            around = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                    around.add(c[nx][ny])
            print((sum(group_num[k] for k in around)+1)%10, end='')
    print()
