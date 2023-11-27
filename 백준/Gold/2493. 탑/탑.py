n = int(input())
towers = list(map(int, input().split()))

stack = []  # 탑들의 정보를 저장할 스택
result = []  # 결과를 저장할 리스트

for i in range(n):
    # 스택이 비어있지 않고, 스택의 top에 있는 탑의 높이가 현재 탑의 높이보다 낮으면 pop
    while stack and stack[-1][1] < towers[i]:
        stack.pop()

    # 스택이 비어있다면 신호를 수신할 탑이 없음
    if not stack:
        result.append(0)
    # 스택의 top에 있는 탑이 신호를 수신할 수 있음
    else:
        result.append(stack[-1][0] + 1)  # 인덱스는 0부터 시작하므로 +1 해줌

    # 현재 탑을 스택에 push. (인덱스, 높이) 정보를 저장
    stack.append((i, towers[i]))

print(*result)