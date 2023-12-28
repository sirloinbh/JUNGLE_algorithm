N = int(input())
CY = 100
SD = 100
for _ in range(N) :
    a,b = map(int, input().split())
    if a > b : 
        SD -= a
    elif a < b :
        CY -= b

print(CY)
print(SD)