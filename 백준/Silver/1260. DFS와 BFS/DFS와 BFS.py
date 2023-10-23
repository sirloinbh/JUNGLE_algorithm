from collections import deque
import sys

def BFS(graph,start):
    visited=[]
    queue = deque([start])

    
    while queue:
        vertex=queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(sorted(graph[vertex]))
    return visited

                
def DFS(graph,start):
    visited=[]
    stack =[start]

    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(sorted(graph[vertex], reverse =True))
    return visited



def main():
    N, M,V = map(int, sys.stdin.readline().split())

    
    graph = {i:[] for i in range(1,N+1)}
    
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    print(" ".join(map(str,DFS(graph,V))))
    print(" ".join(map(str,BFS(graph,V))))
    
main()