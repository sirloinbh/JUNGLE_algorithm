N = int(input())
total_dots = 0
for i in range(1,N+1) :
    total_dots = total_dots + i*(i+1)+i*(i+1)//2
print(total_dots)