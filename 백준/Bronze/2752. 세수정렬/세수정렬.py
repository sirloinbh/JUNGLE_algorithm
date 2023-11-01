# 숫자 세 개를 리스트로 입력 받는다.
numbers = list(map(int, input().split()))

# 리스트를 정렬한다.
numbers.sort()

# 정렬된 리스트를 출력한다.
for num in numbers:
    print(num, end=' ')