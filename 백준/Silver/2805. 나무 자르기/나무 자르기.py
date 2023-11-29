N, M = map(int, input().split())  # 나무의 수 N, 필요한 나무 길이 M
trees = list(map(int, input().split()))  # 나무들의 높이

start, end = 0, max(trees)  # 이분 탐색을 위한 시작, 끝 값 설정
result = 0

while start <= end:
    mid = (start + end) // 2  # 중간 값
    total_length = sum([tree - mid for tree in trees if tree > mid])  # mid 높이로 잘랐을 때의 나무 길이 합

    if total_length >= M:  # 원하는 길이를 얻을 수 있는 경우
        result = mid
        start = mid + 1
    else:  # 원하는 길이를 얻을 수 없는 경우
        end = mid - 1

print(result)