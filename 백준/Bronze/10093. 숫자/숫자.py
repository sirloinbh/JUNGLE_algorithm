# 두 정수 입력 받기
a, b = map(int, input().split())

# a와 b의 위치를 오름차순으로 정렬
if a > b:
    a, b = b, a

# a와 b가 같으면 아무런 수도 출력되지 않아야 함
if a == b:
    print(0)
else:
    # a와 b 사이에 있는 숫자의 개수 출력
    print(b - a - 1)
    # a와 b 사이의 숫자들 출력
    for i in range(a + 1, b):
        print(i, end=' ')