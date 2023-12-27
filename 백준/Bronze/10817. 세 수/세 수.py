A, B, C=map(int, input().split())
if(A>=B) :
    if(C>=A) : print(A)
    elif(B>=C) : print(B)
    else : print(C)

else :
    if(C>=B) : print(B)
    elif(A>=C) : print(A)
    else : print(C)
