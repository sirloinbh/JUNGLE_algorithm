from collections import deque
import sys

def BFS(graph,start,visited):
    queue = deque([start])
    while queue:
        vertex=queue.popleft()
        for neighbor in graph[vertex]:
            if visited[neighbor]==0:
                visited[neighbor]=vertex
                queue.append(neighbor)
    return

def main():
    N= int(sys.stdin.readline())

    
    graph = {i:[] for i in range(1,N+1)}
    visited={i:0 for i in range(1,N+1)}
    
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    BFS(graph,1,visited)
    for i in range(2,N+1):
        print(visited[i])
    
main()