n = int(input())
temp = 0
fibo = 1
if n == 0 : 
    fibo = 0
elif n == 1 :
    fibo = 1
else :
    for i in range(2,n+1) :
        fibo, temp = fibo + temp, fibo
print(fibo)