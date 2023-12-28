N = int(input())
result = [0, 0, 0, 0, 0]

for _ in range(N):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        result[0] += 1
    elif x > 0 and y > 0:
        result[1] += 1
    elif x < 0 and y > 0:
        result[2] += 1
    elif x < 0 and y < 0:
        result[3] += 1
    elif x > 0 and y < 0:
        result[4] += 1

for i in range(1, 5):
    print(f"Q{i}: {result[i]}")
print(f"AXIS: {result[0]}")