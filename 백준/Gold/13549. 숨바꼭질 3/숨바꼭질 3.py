from collections import deque

MAX = 100001
N, K = map(int, input().split())
dist = [0]*MAX

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        if v == K:
            return dist[v]
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not dist[next_step]:
                if next_step == v*2 and v != 0:
                    dist[next_step] = dist[v]
                    q.appendleft(next_step)
                else:
                    dist[next_step] = dist[v] + 1
                    q.append(next_step)

print(bfs(N))
