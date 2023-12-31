A, B = map(int, input().split())
mylist = []
for i in range(1, 101) :
    for j in range(i) :
        mylist.append(i)

print(sum(mylist[A-1:B]))