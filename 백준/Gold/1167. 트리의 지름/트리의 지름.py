import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(v, weight):
    for w, wt in tree[v]:
        if not visited[w]:
            visited[w] = True
            distance[w] = weight + wt
            dfs(w, weight + wt)

V = int(input())
tree = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
distance = [0 for _ in range(V+1)]

for _ in range(V):
    path = list(map(int, input().split()))
    for i in range(1, len(path)-2, 2):
        tree[path[0]].append((path[i], path[i+1]))

visited[1] = True
dfs(1, 0)

max_distance = max(distance)
start = distance.index(max_distance)
visited = [False for _ in range(V+1)]
distance = [0 for _ in range(V+1)]

visited[start] = True
dfs(start, 0)

print(max(distance))
