T = int(input())
jwapyo = []
for _ in range(T) :
    x,y = map(int, input().split())
    jwapyo.append((x,y))
jwapyo.sort()
for x,y in jwapyo :
    print(x,y)