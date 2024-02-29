def find(x):
    if parent[x] == x:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
truth = list(map(int, input().split()))[1:]
parties = [list(map(int, input().split()))[1:] for _ in range(M)]

for party in parties:
    for i in range(len(party) - 1):
        union(party[i], party[i+1])

truth_set = set([find(person) for person in truth])
cnt = 0

for party in parties:
    for person in party:
        if find(person) in truth_set:
            break
    else:
        cnt += 1

print(cnt)
