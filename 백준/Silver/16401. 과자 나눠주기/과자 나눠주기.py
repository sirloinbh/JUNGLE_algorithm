N, M = map(int, input().split())  # 조카의 수 N, 과자의 수 M
snacks = list(map(int, input().split()))  # 과자들의 길이

start, end = 1, max(snacks)  # 이분 탐색을 위한 시작, 끝 값 설정
result = 0

while start <= end:
    mid = (start + end) // 2  # 중간 값
    count = sum([snack // mid for snack in snacks])  # mid 길이로 나눈 과자 수의 합

    if count >= N:  # 조카들에게 나눠줄 수 있는 경우
        result = mid
        start = mid + 1
    else:  # 나눠줄 수 없는 경우
        end = mid - 1

print(result)