from collections import defaultdict

# 입력: 숫자 카드의 개수 N, 숫자 카드의 리스트
N = int(input())
cards = list(map(int, input().split()))

# 딕셔너리 초기화 및 숫자 카드의 개수 기록
count_cards = defaultdict(int)
for card in cards:
    count_cards[card] += 1

# 입력: 탐색할 숫자의 개수 M, 탐색할 숫자 리스트
M = int(input())
numbers = list(map(int, input().split()))

# 결과 출력
for num in numbers:
    print(count_cards[num], end=' ')