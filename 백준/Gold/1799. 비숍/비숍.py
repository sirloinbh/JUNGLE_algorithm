def solve(idx, cnt, color):
    global answer
    if idx >= len(possible[color]):
        answer[color] = max(answer[color], cnt)
        return
    x, y = possible[color][idx]
    if not (ld[x + y] or rd[x - y + N - 1]):
        ld[x + y] = rd[x - y + N - 1] = 1
        solve(idx + 1, cnt + 1, color)
        ld[x + y] = rd[x - y + N - 1] = 0
    solve(idx + 1, cnt, color)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ld = [0] * (2 * N - 1)  # 좌하향 대각선
rd = [0] * (2 * N - 1)  # 우하향 대각선
possible = [[], []]  # 가능한 위치
answer = [0, 0]  # 각 색깔별로 놓을 수 있는 비숍의 최대 개수

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            possible[(i + j) % 2].append((i, j))

solve(0, 0, 0)
solve(0, 0, 1)

print(answer[0] + answer[1])
