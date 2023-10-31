N = int(input())

i = 2
while N != 1:  # N이 1이 아닐 때까지
    if N % i == 0:  # N이 i로 나누어떨어지면
        print(i)  # i는 N의 소인수
        N = N // i  # N을 i로 나눈다.
    else:
        i += 1  # 나누어떨어지지 않으면 i를 1 증가시킨다.