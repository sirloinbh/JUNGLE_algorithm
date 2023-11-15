from collections import deque

# 입력
n, k = map(int, input().split())

# 방문 여부와 시간을 저장하는 리스트
visited = [-1] * 100001

def bfs(n, k):
    queue = deque([n])
    visited[n] = 0  # 시작 위치 방문 시간은 0

    while queue:
        curr = queue.popleft()

        # 현재 위치가 동생의 위치와 같을 경우 종료
        if curr == k:
            return visited[curr]

        # 가능한 3개의 위치로 이동
        for next_pos in [curr - 1, curr + 1, curr * 2]:
            # 범위 내에 있고, 방문하지 않은 위치일 경우
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                visited[next_pos] = visited[curr] + 1
                queue.append(next_pos)

print(bfs(n, k))