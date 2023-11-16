from collections import deque

# 나이트의 이동 방향 (L자 형태)
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

# BFS를 활용한 함수 정의
def bfs(board, start, target):
    q = deque([start])
    board[start[0]][start[1]] = 0  # 시작 위치 방문 표시
    while q:
        x, y = q.popleft()
        # 목표 위치에 도착한 경우 이동 횟수 반환
        if (x, y) == target:
            return board[x][y]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            # 체스판 범위 내에 있으며 방문하지 않은 위치라면
            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    l = int(input())  # 체스판의 한 변의 길이
    board = [[-1]*l for _ in range(l)]  # 체스판 초기화
    start = tuple(map(int, input().split()))  # 시작 위치
    target = tuple(map(int, input().split()))  # 목표 위치
    if start == target:
        print(0)  # 시작 위치와 목표 위치가 같은 경우
    else:
        print(bfs(board, start, target))