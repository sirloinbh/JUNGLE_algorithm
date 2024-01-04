N = int(input())
mylist = []
def divsum(n) :
    sum_ = n
    while n :
        sum_ += n%10
        n = n//10
    return sum_
for i in range(1,N+1) :
    if divsum(i) == N :
        mylist.append(i)
if len(mylist) :
    print(mylist[0])
else :
    print(0)