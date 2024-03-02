def ccw(a, b, c):
    op = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    op -= (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])
    if op > 0:
        return 1
    elif op == 0:
        return 0
    else:
        return -1

def check_intersect(a, b, c, d):
    ab = ccw(a, b, c)*ccw(a, b, d)
    cd = ccw(c, d, a)*ccw(c, d, b)
    if ab == 0 and cd == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return not((b < c) or (d < a))
    return ab <= 0 and cd <= 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
a = [x1, y1]
b = [x2, y2]
c = [x3, y3]
d = [x4, y4]
print(int(check_intersect(a, b, c, d)))
