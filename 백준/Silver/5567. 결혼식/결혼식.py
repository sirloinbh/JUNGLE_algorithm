from collections import deque
import sys

def BFS(graph,start,visited):
    queue = deque([(start,0)])
    visited[start]=True
    cnt=0

    while queue :
        vertex,dep =queue.popleft()
        if dep>2:
            break
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append((neighbor,dep+1))
                visited[neighbor]=True
                if dep+1<=2:
                    cnt+=1
        
    return cnt


def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    
    graph = {i:[] for i in range(1,N+1)}
    visited =[False]*(N+1)
    
    
    for _ in range(M):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    
    
    print(BFS(graph,1,visited))
main()