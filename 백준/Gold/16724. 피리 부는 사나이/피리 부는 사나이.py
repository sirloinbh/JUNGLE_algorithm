import sys

# 재귀 깊이 한도 증가
sys.setrecursionlimit(10**6)

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

# 격자의 크기 및 격자 정보 입력
N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# 유니온-파인드를 위한 부모 배열 초기화
parent = [i for i in range(N * M)]

directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

for i in range(N):
    for j in range(M):
        dir = grid[i][j]
        ni, nj = i + directions[dir][0], j + directions[dir][1]
        # 격자 내 위치를 유지하기 위한 조건 확인 (이 경우는 필요 없을 수 있음)
        if 0 <= ni < N and 0 <= nj < M:
            curr_index = i * M + j
            next_index = ni * M + nj
            union(curr_index, next_index)

# 각 루트 노드를 찾아 집합의 개수 세기
roots = set(find(i) for i in range(N * M))
print(len(roots))
