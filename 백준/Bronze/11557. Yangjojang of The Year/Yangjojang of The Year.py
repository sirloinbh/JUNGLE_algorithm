T = int(input())

for _ in range(T):
    diction = {}
    N = int(input())
    for _ in range(N):
        S, L = input().split()
        diction[S] = int(L)

    max_key = max(diction, key=diction.get)
    print(max_key)
