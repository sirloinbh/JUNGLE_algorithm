N, K = map(int, input().split())
dividor = []
for i in range(1,N+1) :
    if N%i == 0 :
        dividor.append(i)
if len(dividor)>=K :
    print(dividor[K-1])
    
else :
    print(0)