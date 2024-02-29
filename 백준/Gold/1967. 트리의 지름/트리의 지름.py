import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visit = [-1 for _ in range(n+1)]
    queue = deque()
    queue.append(start)
    visit[start] = 0
    _max = [0, 0]

    while queue:
        parent = queue.popleft()
        for node, weight in tree[parent]:
            if visit[node] == -1:
                visit[node] = visit[parent] + weight
                queue.append(node)
                if _max[0] < visit[node]:
                    _max = visit[node], node
    return _max

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

distance, node = bfs(1)
distance, node = bfs(node)
print(distance)
