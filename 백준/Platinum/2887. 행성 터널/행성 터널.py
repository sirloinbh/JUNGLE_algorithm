def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = list(range(n))
edges = []
planets = []

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(1, n):
        cost = abs(planets[j-1][i] - planets[j][i])
        edges.append((cost, planets[j-1][3], planets[j][3]))

edges.sort()
result = 0

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
