T = int(input())
for _ in range(T) :
    H, W, N = map(int, input().split())
    h = 1+ (N-1)//H
    w = 1+(N-1)%H
    print(w*100+h)