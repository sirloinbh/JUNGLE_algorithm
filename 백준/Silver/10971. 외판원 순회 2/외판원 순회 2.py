from itertools import permutations

def tsp(N, W):
    cities = list(range(N))
    min_cost = float('inf')

    for path in permutations(cities):
        if W[path[-1]][path[0]] == 0: 
            continue

        cost = 0
        is_valid = True
        for i in range(N-1):
            if W[path[i]][path[i+1]] == 0: 
                is_valid = False
                break
            cost += W[path[i]][path[i+1]]
        if is_valid:
            cost += W[path[-1]][path[0]]
            min_cost = min(min_cost, cost)

    return min_cost

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
print(tsp(N,W))