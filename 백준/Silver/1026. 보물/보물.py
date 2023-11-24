# 입력
n = int(input())  # 배열의 길이
A = list(map(int, input().split()))  # 배열 A
B = list(map(int, input().split()))  # 배열 B

# A는 오름차순으로, B는 내림차순으로 정렬합니다.
A.sort()
B.sort(reverse=True)

# 정렬된 두 배열의 원소를 순서대로 곱한 후, 그 결과들의 합을 계산합니다.
answer = sum(a * b for a, b in zip(A, B))

# 결과 출력
print(answer)