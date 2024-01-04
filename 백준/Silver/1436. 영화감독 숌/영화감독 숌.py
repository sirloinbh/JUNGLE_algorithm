N = int(input())
mylist = [0]
i =0
while True :
    if '666' in str(i) :
        mylist.append(i)
        if len(mylist) == N+1 :
            break
    i += 1
print(mylist[N])
