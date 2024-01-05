import sys

def paper(N,graph,cntw,cntb) :
    if sum(sum(row) for row in graph) == 0 :
        return (1,0)
    elif sum(sum(row) for row in graph) == sum(len(row) for row in graph) :
        return (0,1)
    else :
        N = N //2
        w,b = paper(N, [row[:N] for row in graph[:N]], 0,0)
        cntw += w
        cntb += b
        w,b = paper(N, [row[N:] for row in graph[:N]], 0,0)
        cntw += w
        cntb += b
        w,b = paper(N, [row[:N] for row in graph[N:]], 0,0)
        cntw += w
        cntb += b
        w,b = paper(N, [row[N:] for row in graph[N:]], 0,0)
        cntw += w
        cntb += b
        return cntw,cntb



N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
for i in range(N) :
    graph[i] = list(map(int, sys.stdin.readline().split()))
    
a,b = paper(N,graph, 0,0)
print(a)
print(b)