T = int(input())
for _ in range(T) :
    N = list(map(int, input().split()))
    N.sort()
    if N[-2] - N[1] >= 4 :
        print("KIN")
    else :
        print(sum(N[1:-1]))