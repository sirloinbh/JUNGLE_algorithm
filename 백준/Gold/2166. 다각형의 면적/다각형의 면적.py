import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.append(points[0])

area = 0
for i in range(N):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    area += (x1*y2 - x2*y1)

print(round(abs(area) / 2, 1))
