import sys
N = int(sys.stdin.readline())
mylist = []
for _ in range(N) :
    x,y = map(int, sys.stdin.readline().split())
    mylist.append((x,y))
    
mylist.sort(key = lambda a : (a[1],a[0]))
for x,y in mylist :
    print(x,y)