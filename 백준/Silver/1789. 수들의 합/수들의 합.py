S = int(input())
if S == 1 :
    print(1)
else :
    for i in range(1, S+1) :
        if i*(i+1)/2 >S :
            print(i-1)
            break 