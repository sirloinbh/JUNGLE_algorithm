import math
import sys

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

def distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a * a) + (b * b))

N = int(sys.stdin.readline())
stars = []
parent = [0] * N
edges = []

for i in range(N):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

length = len(stars)

for i in range(length - 1):
    for j in range(i + 1, length):
        edges.append((i, j, distance(stars[i], stars[j])))

for i in range(N):
    parent[i] = i

edges.sort(key=lambda data: data[2])

result = 0
for a, b, cost in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print("%0.2f" % result)
