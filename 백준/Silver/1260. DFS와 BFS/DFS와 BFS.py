from collections import deque

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            # 인접한 정점들을 스택에 추가합니다.
            # 여기서 역순으로 추가하는 이유는 작은 번호의 정점부터 방문하기 위함입니다.
            stack.extend(sorted(graph[vertex], reverse=True))
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            # 인접한 정점들을 큐에 추가합니다.
            queue.extend(sorted(graph[vertex]))
    return visited

def dfs_bfs_with_io():
    # 정점의 수, 간선의 수, 시작 정점 번호를 입력받습니다.
    N, M, V = map(int, input().split())
    
    # 그래프를 초기화합니다.
    graph = {i: [] for i in range(1, N + 1)}

    # 간선 정보를 입력받아 그래프를 구성합니다.
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # DFS와 BFS 결과를 출력합니다.
    print(" ".join(map(str, dfs(graph, V))))
    print(" ".join(map(str, bfs(graph, V))))

# 주석 처리하여 실행 오류를 막습니다.
dfs_bfs_with_io()