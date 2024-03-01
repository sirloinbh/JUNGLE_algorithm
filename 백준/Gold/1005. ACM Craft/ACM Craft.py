import sys
from collections import deque

def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = building[i]

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + building[i])
            if indegree[i] == 0:
                q.append(i)


T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    building = [0] + list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    dp = [0 for _ in range(N+1)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X].append(Y)
        indegree[Y] += 1

    W = int(sys.stdin.readline())
    topology_sort()
    print(dp[W])
