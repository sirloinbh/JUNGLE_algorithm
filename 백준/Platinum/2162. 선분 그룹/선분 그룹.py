import sys

input = sys.stdin.readline

# 두 점 p1, p2를 지나는 선분과 점 p3의 상대적 위치
def ccw(p1, p2, p3):
    op = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]
    op -= (p1[1]*p2[0] + p2[1]*p3[0] + p3[1]*p1[0])
    if op > 0:
        return 1
    elif op < 0:
        return -1
    else:
        return 0

# 선분 (p1, p2)와 선분 (p3, p4)의 교차 여부 판별
def is_intersect(p1, p2, p3, p4):
    ab = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    cd = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if ab == 0 and cd == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        return p1 <= p4 and p3 <= p2
    return ab <= 0 and cd <= 0

# 유니온-파인드 구현
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        group_size[x] += group_size[y]

n = int(input())
parent = list(range(n))
group_size = [1] * n
lines = []

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append(((x1, y1), (x2, y2)))

for i in range(n):
    for j in range(i+1, n):
        if is_intersect(lines[i][0], lines[i][1], lines[j][0], lines[j][1]):
            union(i, j)

# 그룹의 수와 가장 큰 그룹의 크기 계산
groups = set(find(i) for i in range(n))
max_group_size = max(group_size[find(i)] for i in range(n))

print(len(groups))
print(max_group_size)
