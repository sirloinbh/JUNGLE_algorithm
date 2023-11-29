# 집합 A와 B의 원소 개수를 입력 받습니다.
n, m = map(int, input().split())

# 집합 A의 원소들을 입력받아 set 자료구조에 저장합니다.
A = set(map(int, input().split()))
# 집합 B의 원소들을 입력받아 set 자료구조에 저장합니다.
B = set(map(int, input().split()))

# 집합 A에서 집합 B의 원소들을 제거합니다.
# 이 연산 후 A는 A - B의 결과가 됩니다.
A -= B

# 결과로 나온 집합 A의 원소 개수를 출력합니다.
print(len(A))
# 집합 A의 원소들을 오름차순으로 정렬하여 출력합니다.
print(' '.join(map(str, sorted(A))))