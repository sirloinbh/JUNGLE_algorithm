import math

def count_crossings(x1, y1, x2, y2, circles):
    count = 0
    for cx, cy, r in circles:
        dist_a = math.sqrt((x1 - cx)**2 + (y1 - cy)**2)
        dist_b = math.sqrt((x2 - cx)**2 + (y2 - cy)**2)

        inside_a = dist_a < r
        inside_b = dist_b < r

        if inside_a != inside_b:
            count += 1
    return count

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    circles = []
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        circles.append((cx, cy, r))
    result = count_crossings(x1, y1, x2, y2, circles)
    print(result)
