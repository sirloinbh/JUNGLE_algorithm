# 건물의 수를 입력받음
n = int(input())
# n개의 건물 높이를 입력받아 리스트로 저장
buildings = [int(input()) for _ in range(n)]

# 건물 높이를 저장할 스택 초기화
stack = []
# 결과값(각 건물에서 오른쪽으로 볼 수 있는 건물의 총 수) 초기화
result = 0

# 모든 건물을 순회
for building in buildings:
    # 현재 건물의 높이가 스택의 top(맨 위) 건물의 높이보다 크거나 같은 경우
    # 현재 건물 뒤에 있는 건물들은 스택의 top 건물을 볼 수 없으므로 pop
    while stack and stack[-1] <= building:
        stack.pop()
    
    # 이 시점에서의 스택에는 현재 건물보다 높아서 볼 수 있는 건물들만 남게됨
    # 따라서 스택의 길이(남아있는 건물의 수)를 결과에 더함
    result += len(stack)
    
    # 현재 건물의 높이를 스택에 추가
    stack.append(building)

# 각 건물에서 오른쪽으로 볼 수 있는 건물의 총 수를 출력
print(result)