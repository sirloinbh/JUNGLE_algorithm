def is_available(current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        # 같은 열에 있거나 대각선에 위치하는지 확인
        if candidate[queen_row] == current_col or \
            candidate[queen_row] - queen_row == current_col - current_row or \
            candidate[queen_row] + queen_row == current_col + current_row:
            return False
    return True

def DFS(N, current_row):
    global result
    if current_row == N:
        result += 1
        return
    for candidate_col in range(N):
        if is_available(candidate_col):
            candidate.append(candidate_col)
            DFS(N, current_row + 1)
            candidate.pop()

N = int(input())
result = 0
candidate = []
DFS(N, 0)
print(result)
