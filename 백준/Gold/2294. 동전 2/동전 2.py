from collections import deque

# BFS를 통해 최소 동전 개수를 찾는 함수
def bfs_minimum_coins(coins, k):
    # dist[i]는 합 i를 만드는데 필요한 최소 동전 개수
    # 처음에는 모든 값들을 -1로 초기화 (아직 방문하지 않은 상태)
    dist = [-1] * (k + 1)
    # 0원을 만들기 위한 동전 개수는 0이므로 초기값 설정
    dist[0] = 0
    queue = deque([0])  # BFS를 위한 큐, 0원부터 시작

    while queue:
        current = queue.popleft()  # 현재 금액
        for coin in coins:  # 각 동전에 대해
            next_value = current + coin  # 현재 금액에 동전을 더한 값
            # 다음 값이 목표 금액 이하이고 아직 방문하지 않은 상태라면
            if next_value <= k and dist[next_value] == -1:
                # 다음 값에 대한 최소 동전 개수는 현재 금액의 동전 개수 + 1
                dist[next_value] = dist[current] + 1
                queue.append(next_value)  # BFS를 위해 큐에 추가

    return dist[k]  # 목표 금액에 대한 최소 동전 개수 반환

def find_minimum_coins_with_bfs():
    n, k = map(int, input().split())  # 동전의 종류 개수 n, 목표 금액 k 입력받기
    coins = [int(input()) for _ in range(n)]  # 각 동전의 가치를 입력받아 리스트에 저장

    result = bfs_minimum_coins(coins, k)  # bfs 함수를 통해 결과 계산
    print(result)  # 결과 출력

# 주석 처리하여 실행 오류를 막습니다.
find_minimum_coins_with_bfs()