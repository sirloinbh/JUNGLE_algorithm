import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]

count = 0
for _ in range(P):
    gi = int(input())
    docking = find(gi)
    if docking != 0:
        union(docking-1, docking)
        count += 1
    else:
        break

print(count)
