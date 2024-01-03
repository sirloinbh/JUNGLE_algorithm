N = int(input())
mylist = []
body = []
for _ in range(N) :
    x,y = map(int, input().split())
    mylist.append((x,y))

for i in range(len(mylist)) :
    order = 1
    for j in range(len(mylist)) :
        if mylist[i][0] < mylist[j][0] and mylist[i][1] < mylist[j][1] :
            order += 1
    body.append(order)
print(*body)