import sys
input = sys.stdin.readline
INF = int(1e9)

# 지역의 개수 n, 수색 범위 m, 길의 개수 r을 입력받기
n, m, r = map(int, input().split())
# 각 지역에 있는 아이템의 개수 입력받기
items = [0] + list(map(int, input().split()))
# 최단 거리 테이블을 모두 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 각 지역에서 시작했을 때 수집할 수 있는 아이템의 최대 개수 계산
max_value = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            temp += items[j]
    max_value = max(max_value, temp)

print(max_value)
