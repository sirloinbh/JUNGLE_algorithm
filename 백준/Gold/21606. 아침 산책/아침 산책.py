from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

# DFS 함수 정의
def DFS(v:int):
    indoor = 0  # 현재 노드와 연결된 실내 노드의 수를 저장하기 위한 변수
    for i in net[v]:  # 현재 노드와 연결된 모든 노드를 순회
        if A[i-1] == 0:  # 연결된 노드가 실외인 경우
            if i not in visited:  # 해당 노드를 방문하지 않았다면
                visited.add(i)  # 방문 처리
                indoor += DFS(i)  # 해당 노드에서 DFS 수행
        else:  # 연결된 노드가 실내인 경우
            indoor += 1  # 실내 노드 카운트 증가

    return indoor

N = int(input())
A = list(map(int, list(input())))  # 각 장소의 실내/실외 정보 저장
net = defaultdict(list)  # 각 노드와 연결된 노드의 정보를 저장하기 위한 딕셔너리
route_count = 0  # 총 경로의 수를 저장하기 위한 변수

# 노드 간의 연결 정보 입력 받기
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    net[u].append(v)
    net[v].append(u)
    if A[u-1] == 1 and A[v-1] == 1:  # 두 노드가 모두 실내인 경우
        route_count += 2  # 경로 수 2 증가 (양방향이므로)

visited = set()  # 방문한 노드 정보를 저장하기 위한 집합
for i in range(1, N+1):
    indoor = 0
    if A[i-1] == 0:  # 현재 노드가 실외인 경우
        if i not in visited:  # 방문하지 않았다면
            visited.add(i)  # 방문 처리
            indoor = DFS(i)  # 현재 노드에서 DFS 수행

    route_count += indoor*(indoor-1)  # 산책 경로의 수 계산 및 추가

print(route_count)  # 총 경로의 수 출력