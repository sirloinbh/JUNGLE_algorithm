import sys
def main():
    N =int(sys.stdin.readline())

    
    graph = [[] for i in range(1,N+1)]
    
    for i in range(N):
        a= list(map(int, sys.stdin.readline().split()))
        graph[i]=a
    for _ in range(2):
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if graph[i][j]==1 and graph[j][k]==1 :
                        graph[i][k]=1

    for i in range(N):
        print (" ".join(map(str,graph[i])))
    
main()