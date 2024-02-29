from collections import deque

def bfs():
    queue = deque()
    queue.append(1)
    dist[1] = 0
    while queue:
        x = queue.popleft()
        for i in range(1, 7):
            y = x + i
            if y > 100:
                continue
            y = check[y]
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                queue.append(y)

N, M = map(int, input().split())
dist = [-1]*101
check = [i for i in range(101)]
for _ in range(N+M):
    x, y = map(int, input().split())
    check[x] = y
bfs()
print(dist[100])
