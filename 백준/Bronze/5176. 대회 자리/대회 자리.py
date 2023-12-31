K = int(input())
for _ in range(K) :
    P, M = map(int, input().split())
    appliance = [int(input()) for _ in range(P)]
    appliance = set(appliance)
    print(P-len(appliance))