import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for i in range(1, m+1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i)
        break
    else:
        union(a, b)
else:
    print(0)
