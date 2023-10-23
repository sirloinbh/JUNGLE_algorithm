n = int(input())
numbers = list(map(int, input().split()))
ops_count = list(map(int, input().split()))

INF = float('inf')
max_val = -INF
min_val = INF

def dfs(index, result, add, sub, mul, div):
    global max_val, min_val

    # 모든 연산을 완료한 경우
    if index == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    # 각 연산자에 대해 재귀적으로 dfs 수행
    if add:
        dfs(index + 1, result + numbers[index], add - 1, sub, mul, div)
    if sub:
        dfs(index + 1, result - numbers[index], add, sub - 1, mul, div)
    if mul:
        dfs(index + 1, result * numbers[index], add, sub, mul - 1, div)
    if div:
        if result < 0:  # 음수 나눗셈 처리
            dfs(index + 1, -(-result // numbers[index]), add, sub, mul, div - 1)
        else:
            dfs(index + 1, result // numbers[index], add, sub, mul, div - 1)

dfs(1, numbers[0], ops_count[0], ops_count[1], ops_count[2], ops_count[3])
print(max_val)
print(min_val)
