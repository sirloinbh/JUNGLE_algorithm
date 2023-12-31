T = int(input())
for _ in range(T) :
    n = int(input())
    position = list(map(int, input().split()))
    print(2*(max(position)-min(position)))