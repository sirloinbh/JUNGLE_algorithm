from math import sqrt
M = int (input ())
N = int (input ())
mult = []
for i in range (M, N+1) :
    for j in range(1, int(sqrt(N))+1) :
        if i == j*j :
            mult.append(i)

if sum(mult) == 0 :
    print(-1)
else : 
    print(sum(mult))
    print(mult[0])