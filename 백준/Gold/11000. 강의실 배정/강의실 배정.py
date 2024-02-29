import heapq
import sys

N = int(sys.stdin.readline())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
classes.sort(key=lambda x: x[0])

rooms = [] 
heapq.heappush(rooms, classes[0][1])

for i in range(1, N):
    if rooms[0] <= classes[i][0]: 
        heapq.heappop(rooms) 

    heapq.heappush(rooms, classes[i][1])

print(len(rooms))