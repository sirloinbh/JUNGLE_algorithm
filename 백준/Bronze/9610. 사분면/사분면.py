N = int(input())
result = [0 for _ in range(6)]

for _ in range(N) :
    x, y = map(int, input().split())
    if x >0 :
        if y>0 : result[1]+=1
        elif y<0 : result[4] += 1
        else : result[5] += 1
    elif x<0 :
        if y>0 : result[2]+=1
        elif y < 0 : result[3] += 1
        else :result[5] += 1
    else : result[5] +=1

for i in range(1,len(result)-1) :
    print("Q%d: %d" %(i,result[i]))
print("AXIS: %d" %(result[-1]))