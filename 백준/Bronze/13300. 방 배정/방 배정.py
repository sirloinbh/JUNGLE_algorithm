N, K = map(int, input().split())
students = [[0] * 6 for _ in range(2)]

rooms = 0

for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y-1] += 1

for i in range(2):  
    for j in range(6):  
        rooms += (students[i][j] // K) + (1 if students[i][j] % K else 0)

print(rooms)