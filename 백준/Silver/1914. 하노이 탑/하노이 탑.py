def hanoi1(n):
    if(n==1) : return 1;
    else : return 2*hanoi1(n-1)+1

def hanoi2(n,x,y):

    if n>20 :
        return False
    else :
        if n>1 : hanoi2(n-1,x,6-x-y)
        print(x,y)
        if n>1 : hanoi2(n-1,6-x-y,y)
N=int(input())
print(hanoi1(N))
hanoi2(N,1,3)