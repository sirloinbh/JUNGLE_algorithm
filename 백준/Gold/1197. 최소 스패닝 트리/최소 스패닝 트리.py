class UnionFind:
    def __init__(self, n):
        # 각 정점의 부모 노드 정보를 저장하는 리스트입니다.
        # 초기에는 각 정점은 자기 자신을 부모로 가집니다.
        self.parent = [i for i in range(n)]

    def find(self, x):
        # x의 루트 노드를 찾아 반환하는 함수입니다.
        # '경로 압축 기법'을 사용하여 루트 노드를 찾는 도중에 방문한 노드들을 직접 루트 노드에 연결합니다.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # x와 y의 루트 노드를 찾아 합치는 함수입니다.
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

def kruskal(graph, edges):
    # Kruskal 알고리즘을 사용하여 MST의 가중치 합을 계산합니다.
    uf = UnionFind(len(graph) + 1)  # 정점 번호가 1부터 시작하므로 +1을 해줍니다.
    mst_weight = 0
    for edge in sorted(edges, key=lambda x: x[2]):  # 간선을 가중치 순으로 정렬합니다.
        u, v, w = edge
        # 선택한 간선이 사이클을 형성하지 않는 경우 MST에 추가합니다.
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += w
    return mst_weight

def main():
    # 정점의 수(V)와 간선의 수(E)를 입력받습니다.
    V, E = map(int, input().split())
    
    # 간선의 정보를 저장할 리스트를 초기화합니다.
    edges = []
    
    # 간선의 정보를 입력받아 리스트에 저장합니다.
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    # Kruskal 알고리즘을 이용하여 최소 스패닝 트리의 가중치 합을 계산합니다.
    mst_weight = kruskal({i: [] for i in range(1, V + 1)}, edges)
    
    # 결과를 출력합니다.
    print(mst_weight)

# main 함수를 호출하여 입력과 출력을 진행합니다.
main()