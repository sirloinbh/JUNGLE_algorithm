from collections import deque

def bfs(building, w, h):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    fire = deque()
    person = deque()

    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire.append((i, j))
            elif building[i][j] == '@':
                person.append((i, j, 0))

    while person:
        # Spread fire
        for _ in range(len(fire)):
            x, y = fire.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.':
                    building[nx][ny] = '*'
                    fire.append((nx, ny))

        # Move person
        for _ in range(len(person)):
            x, y, t = person.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # Check if Sanggeun reaches the boundary of the building
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    return t + 1
                if building[nx][ny] == '.':
                    person.append((nx, ny, t + 1))
                    building[nx][ny] = '@'

    return "IMPOSSIBLE"

# Read input
t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]
    print(bfs(building, w, h))
