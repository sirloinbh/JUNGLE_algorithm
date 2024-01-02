N = int(input())
def hansu(n) :
    if 1 <= n <100 : 
        return True
    elif 100 <= n <= 1000 :
        if (n//100 - (n//10)%10) == ((n//10)%10 - n%10) :
            return True
        else :
            return False
cnt = 0
for i in range(1,N+1) :
    if hansu(i) :
        cnt+=1
print(cnt)