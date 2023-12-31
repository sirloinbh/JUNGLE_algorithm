T = int(input())
for _ in range(T) :
    n = int(input())
    n = bin(n)
    n = str(n)
    n= n[::-1]
    for i in range(len(n)) :
        if n[i] == '1' : print(i, end = ' ')