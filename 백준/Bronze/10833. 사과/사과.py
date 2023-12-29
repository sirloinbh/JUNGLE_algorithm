N = int(input())
rest_apple = 0
for _ in range(N) :
    std, apple = map(int,input().split())
    rest_apple += apple%std
print(rest_apple)