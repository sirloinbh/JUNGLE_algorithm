fibonacci = [0,1]

n = int(input())
for i in range(2,n+1) :
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
print(fibonacci[n])