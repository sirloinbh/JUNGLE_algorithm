import heapq

n = int(input())

heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

result = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    heapq.heappush(heap, a+b)
    result += a + b

print(result)