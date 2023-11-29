# 입력을 받습니다.
n = int(input())
# 상근이의 카드를 오름차순으로 정렬합니다.
cards = sorted(list(map(int, input().split())))

# 비교할 숫자들의 개수를 입력 받습니다.
m = int(input())
# 비교할 숫자들을 리스트로 받습니다.
numbers = list(map(int, input().split()))

# 이분 탐색 함수 정의
def binary_search(array, target, start, end):
    while start <= end:  # 시작점이 끝점보다 작거나 같을 때까지
        mid = (start + end) // 2  # 중앙값 설정
        # 중앙값이 목표값과 일치할 경우
        if array[mid] == target:
            return True
        # 중앙값이 목표값보다 큰 경우
        elif array[mid] > target:
            end = mid - 1  # 끝점을 중앙값보다 하나 앞으로 설정
        # 중앙값이 목표값보다 작은 경우
        else:
            start = mid + 1  # 시작점을 중앙값보다 하나 뒤로 설정
    # while loop 종료 후, 탐색 실패
    return False

# 각 숫자에 대해서 이분 탐색을 수행
for number in numbers:
    # 해당 숫자가 카드에 존재하면
    if binary_search(cards, number, 0, n-1):
        print(1, end=' ')  # 1 출력
    else:  # 존재하지 않으면
        print(0, end=' ')  # 0 출력