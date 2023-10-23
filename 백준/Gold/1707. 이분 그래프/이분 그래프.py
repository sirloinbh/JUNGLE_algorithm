from collections import deque
import sys

def BFS(graph,start,color):
    
    queue = deque([start])
    color[start]=1
    while queue:
        
        vertex=queue.popleft()
        for neighbor in graph[vertex]:
            if color[neighbor]==0:
                color[neighbor]=-color[vertex]
                queue.append(neighbor)
            elif color[neighbor]==color[vertex]:
                return False  
    return True

def main():
    K = int(sys.stdin.readline())
    for _ in range(K):
        V, E = map(int, sys.stdin.readline().split())
        graph = {i:[] for i in range(1,V+1)}
        color=[0]*(V+1)
        for _ in range(E):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append(v)
            graph[v].append(u)
        is_bipartite = True
        for i in range(1,V+1):
            if color[i]==0:
                if not BFS(graph,i,color):
                    is_bipartite=False
                    break
        print("YES" if is_bipartite else "NO")
                
    
main()