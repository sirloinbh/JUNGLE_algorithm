n = int(input())

# 입력 수열을 저장하기 위한 리스트
sequence = [int(input()) for _ in range(n)]

stack = []  # 스택
result = []  # 결과 ('+'와 '-')를 저장할 리스트
current = 1  # 현재 처리할 숫자

for num in sequence:
    # 현재 숫자가 주어진 수열의 값에 도달할 때까지 push
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    # 스택의 top 값이 주어진 수열의 값과 같으면 pop
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    # 스택의 top 값이 주어진 수열의 값과 다르다면, 해당 수열을 만들 수 없음
    else:
        print("NO")
        exit(0)

# 결과 출력
for r in result:
    print(r)