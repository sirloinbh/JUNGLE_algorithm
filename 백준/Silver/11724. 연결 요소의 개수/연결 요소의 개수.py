from collections import deque
import sys

def BFS(graph,start,visited):
    queue = deque([start])
    visited[start]=True
    
    while queue:
        vertex=queue.popleft()
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=True


def main():
    N, M = map(int, sys.stdin.readline().split())

    
    graph = {i:[] for i in range(1,N+1)}
    visited =[False]*(N+1)
    cnt=0
    
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1,N+1):
        if not visited[i]:
            BFS(graph,i,visited)
            cnt+=1
    print(cnt)
main()