import heapq
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    min_heap = []
    max_heap = []
    visited = dict()
    k = int(sys.stdin.readline())
    for _ in range(k):
        op, n = sys.stdin.readline().split()
        n = int(n)
        if op == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            if n in visited:
                visited[n] += 1
            else:
                visited[n] = 1
        else:
            if n == 1:
                while max_heap and visited[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
            else:
                while min_heap and visited[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0]] -= 1
                    heapq.heappop(min_heap)
    while max_heap and visited[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and visited[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print('EMPTY')
