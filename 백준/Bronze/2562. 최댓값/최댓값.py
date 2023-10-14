a = []
for _ in range(1,10) :
    b=int(input())
    a.append(b)


print(max(a))
print(a.index(max(a))+1)
