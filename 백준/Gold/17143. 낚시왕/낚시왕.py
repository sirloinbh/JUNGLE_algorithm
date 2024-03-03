R, C, M = map(int, input().split())
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append((r-1, c-1, s, d, z))

directions = [(0,0), (-1,0), (1,0), (0,1), (0,-1)]
result = 0

def move_sharks():
    global sharks
    new_sharks = {}
    for r, c, s, d, z in sharks:
        nr, nc = r, c
        speed = s
        
        if d <= 2:  # 상하 이동
            speed %= (R-1) * 2
            for _ in range(speed):
                if nr == 0: d = 2
                if nr == R-1: d = 1
                nr += directions[d][0]
        else:  # 좌우 이동
            speed %= (C-1) * 2
            for _ in range(speed):
                if nc == 0: d = 3
                if nc == C-1: d = 4
                nc += directions[d][1]
        
        if (nr, nc) in new_sharks:
            if new_sharks[(nr, nc)][4] < z:
                new_sharks[(nr, nc)] = (nr, nc, s, d, z)
        else:
            new_sharks[(nr, nc)] = (nr, nc, s, d, z)
            
    sharks = list(new_sharks.values())

for fisher in range(C):
    # 상어 잡기
    sharks.sort()
    for i, (r, c, s, d, z) in enumerate(sharks):
        if c == fisher:
            result += z
            sharks.pop(i)
            break
    
    # 상어 이동
    move_sharks()

print(result)
