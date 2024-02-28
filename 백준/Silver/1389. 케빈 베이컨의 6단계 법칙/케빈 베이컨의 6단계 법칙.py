INF = float('inf')

def floyd_warshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

def find_kevin_bacon(graph, n):
    min_kevin_bacon = INF
    kevin_bacon_user = 0
    
    for i in range(n):
        sum_kevin_bacon = sum(graph[i])
        if sum_kevin_bacon < min_kevin_bacon:
            min_kevin_bacon = sum_kevin_bacon
            kevin_bacon_user = i + 1
            
    return kevin_bacon_user

def main():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1
    
    for i in range(n):
        graph[i][i] = 0
    
    floyd_warshall(graph, n)
    
    kevin_bacon_user = find_kevin_bacon(graph, n)
    
    print(kevin_bacon_user)

if __name__ == "__main__":
    main()
