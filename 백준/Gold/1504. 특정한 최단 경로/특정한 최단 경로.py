import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수와 간선의 개수를 입력받기
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 간선 정보를 입력받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 반드시 거쳐야 하는 두 개의 정점 v1, v2
v1, v2 = map(int, input().split())

# 다익스트라 알고리즘
def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

# 시작점에서 v1, v2까지의 최단 거리, v1과 v2 사이의 최단 거리, 그리고 v1, v2에서 도착점까지의 최단 거리 계산
start_to_v1 = dijkstra(1)[v1]
start_to_v2 = dijkstra(1)[v2]
v1_to_v2 = dijkstra(v1)[v2]
v1_to_n = dijkstra(v1)[n]
v2_to_n = dijkstra(v2)[n]

# 두 가지 경로 중 더 짧은 경로 선택
path1 = start_to_v1 + v1_to_v2 + v2_to_n
path2 = start_to_v2 + v1_to_v2 + v1_to_n

# 가능한 최단 경로가 없는 경우 -1 출력
if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))
