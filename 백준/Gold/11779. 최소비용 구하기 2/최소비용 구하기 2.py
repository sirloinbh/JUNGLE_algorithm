import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                route[i[0]] = now
                heapq.heappush(heap_data, (cost, i[0]))

N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
route = [0 for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

start, end = map(int, input().split())

dijkstra(start)

path = [end]
while end != start:
    path.append(route[end])
    end = route[end]

print(distance[path[0]])
print(len(path))
for i in path[::-1]:
    print(i, end=' ')
