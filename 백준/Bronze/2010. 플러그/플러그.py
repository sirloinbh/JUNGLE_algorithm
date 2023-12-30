import sys
N = int(sys.stdin.readline().strip())
multi = 0
for _ in range(N) :
    multi +=int(sys.stdin.readline().strip())
print(multi - N+1)