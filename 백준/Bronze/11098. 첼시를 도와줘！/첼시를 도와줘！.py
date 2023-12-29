n = int(input())
for _ in range(n) :
    mydic = {}
    p = int(input())
    for _ in range(p) :
        c, m = map(str,input().split())
        c = int(c)
        mydic[c] = m
    
    print(mydic[max(mydic.keys())])