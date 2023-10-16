N=int(input())
a=[]
for i in range(N) :
    b=int(input())
    a.append(b)
for j in range(len(a)) :
    for k in range(1,len(a)):
        if a[k]<a[k-1]:
            a[k],a[k-1]=a[k-1],a[k]
for i in range(N) :
    print(a[i])