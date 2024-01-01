T = int(input())
for _ in range(T) :
    N,M = map(int, input().split())
    cnt = 0
    for i in range(N,M+1) :
        cnt += str(i).count('0')
    print(cnt)