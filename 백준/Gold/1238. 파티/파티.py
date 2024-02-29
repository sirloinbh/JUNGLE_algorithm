import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance

N, M, X = map(int, input().split())
graph = [[] for i in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

result = [0] * (N + 1)
for i in range(1, N + 1):
    go = dijkstra(i)
    back = dijkstra(X)
    result[i] = go[X] + back[i]

print(max(result))
