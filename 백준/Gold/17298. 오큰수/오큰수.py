n = int(input())
sequence = list(map(int, input().split()))

# 결과를 저장할 리스트, 초기값은 모두 -1로 설정
result = [-1] * n

# 오큰수를 찾지 못한 수열의 인덱스를 저장할 스택 초기화
stack = []

for i in range(n):
    # 스택이 비어있지 않고, 현재 숫자가 스택의 top에 있는 인덱스의 숫자보다 크면
    # 스택의 top에 있는 인덱스의 오큰수를 현재 숫자로 설정
    while stack and sequence[stack[-1]] < sequence[i]:
        result[stack.pop()] = sequence[i]
    # 현재 인덱스를 스택에 push
    stack.append(i)

# 출력
print(' '.join(map(str, result)))