import sys
N = int(sys.stdin.readline())
mydic = {i:0 for i in range(1,10001)}
for _ in range(N) :
    n = int(sys.stdin.readline())
    if n in mydic.keys() :
        mydic[n]+=1

for i in mydic.keys():
    for j in range(mydic[i]) :
        print(i)