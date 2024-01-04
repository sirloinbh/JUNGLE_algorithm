T =int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    resident = [[0]*n for _ in range(k+1)]
    
    for i in range(n):
        resident[0][i] = i + 1
    
    for i in range(1, k+1):
        for j in range(n):
            resident[i][j] = sum(resident[i-1][:j+1])
    
    print(resident[k][n-1])

