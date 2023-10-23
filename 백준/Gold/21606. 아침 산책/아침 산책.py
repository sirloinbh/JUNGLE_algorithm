import sys
from collections import deque

def BFS(graph, start, A):
    visited = set()
    queue = deque([start])
    cnt = 0

    if A[start-1] == 0:
        return cnt

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)

            if A[vertex-1] == 1 and vertex != start:
                cnt += 1
            else:
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    return cnt

def main():
    N = int(sys.stdin.readline())
    A = [int(digit) for digit in sys.stdin.readline().strip()]
    
    graph = {i: [] for i in range(1, N+1)}
    cnt = 0
    
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, N+1):
        cnt += BFS(graph, i, A)

    print(cnt)

main()