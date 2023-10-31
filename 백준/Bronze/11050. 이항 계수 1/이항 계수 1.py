# 팩토리얼을 계산하는 함수
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

# 입력 받기
N, K = map(int, input().split())

# 이항계수 계산
result = factorial(N) // (factorial(K) * factorial(N-K))

# 결과 출력
print(result)