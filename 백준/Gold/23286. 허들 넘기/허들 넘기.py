INF = int(1e9)

def input_data():
    global N, M, T, DP
    N, M, T = map(int, input().split())
    DP = [[INF] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        DP[i][i] = 0
        
    for _ in range(M):
        U, V, H = map(int, input().split())
        DP[U][V] = H

def settings():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                DP[i][j] = min(DP[i][j], max(DP[i][k], DP[k][j]))

def query():
    for _ in range(T):
        S, E = map(int, input().split())
        if DP[S][E] == INF:
            print(-1)
        else:
            print(DP[S][E])

if __name__ == "__main__":
    input_data()
    settings()
    query()
