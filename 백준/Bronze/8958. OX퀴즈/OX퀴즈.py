N=int(input())

for i in range(N) :
    score=0
    total=0
    OX= input()
    for j in range(0, len(OX)):
        if OX[j]=="O":
            score+=1
            total+=score
        else:
            score=0
    print(total)