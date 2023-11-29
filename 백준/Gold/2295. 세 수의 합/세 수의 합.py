# sys 모듈을 사용하여 입력 속도를 높이기 위한 설정
import sys
input = sys.stdin.readline

# 숫자들의 개수 입력 받기
n = int(input())

# 입력받은 숫자들을 저장할 집합 (중복 제거 목적)
u = set()

# 결과를 저장할 리스트
ans = []

# 입력받은 숫자들을 집합에 저장
for i in range(n):
    u.add(int(input()))

# 두 숫자의 합을 저장할 집합 (sums)
sums = set()
for i in u:
    for j in u:
        # 두 숫자의 합을 sums 집합에 저장
        sums.add(i + j)

# 집합 u의 숫자들 중에서, 어떤 두 숫자의 차가 sums에 존재하는 숫자를 찾기
for i in u:
    for j in u:
        if (i - j) in sums:
            ans.append(i)

# 결과 리스트(ans)를 정렬하고 최댓값 출력
ans.sort()
print(ans[-1])