from collections import deque

A, B = map(int, input().split())

def bfs(A, B):
    queue = deque([(A, 1)])
    while queue:
        x, y = queue.popleft()
        if x == B:
            return y
        if x*2 <= B:
            queue.append((x*2, y+1))
        if int(str(x)+'1') <= B:
            queue.append((int(str(x)+'1'), y+1))
    return -1

print(bfs(A, B))
