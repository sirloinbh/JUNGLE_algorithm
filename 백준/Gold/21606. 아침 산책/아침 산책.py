import sys

def DFS(graph,start,A):
    visited=[]
    stack =[start]
    cnt=0
    if A[start]==0:
        return cnt 
    else:

        while stack:
            vertex=stack.pop()
            if (vertex not in visited) and (A[vertex]==0):
                visited.append(vertex)
                stack.extend(sorted(graph[vertex], reverse =True))
            else:
                cnt+=1
                return cnt
        

def main():
    N= int(sys.stdin.readline())
    A = [int(digit) for digit in sys.stdin.readline().strip()]
    
    graph = {i:[] for i in range(1,N+1)}
    cnt=0
    
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(N):
        cnt+=DFS(graph,i,A)
    print(cnt*2)
main()