N = int(input())
cnt = 0
maximum = 1
while N > maximum :
    cnt +=1 
    maximum += 6*cnt
print(cnt+1)