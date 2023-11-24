import heapq  # heapq 모듈을 사용하여 우선순위 큐(힙)를 구현

# 입력 받기: n은 카드의 수, m은 연산의 수
n, m = map(int, input().split())

# 카드의 초기 정보를 리스트로 받아옴
cards = list(map(int, input().split()))

# 카드 리스트를 최소 힙으로 변환
# 이 힙에서 가장 작은 값을 효율적으로 추출할 수 있음
heapq.heapify(cards)

# m번의 연산을 수행
for _ in range(m):
    # 힙에서 가장 작은 값(card1) 추출
    card1 = heapq.heappop(cards)
    
    # 힙에서 그 다음으로 작은 값(card2) 추출
    card2 = heapq.heappop(cards)
    
    # card1과 card2를 합친 값을 두 번 힙에 넣음
    # 문제의 조건에 따라 동일한 값 두 개를 추가
    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

# 모든 카드의 값을 합산하여 결과 출력
print(sum(cards))