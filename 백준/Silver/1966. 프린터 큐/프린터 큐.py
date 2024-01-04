from collections import deque
T = int(input())
for _ in range(T) :
    N,M = map(int, input().split())
    docu = list(map(int, input().split()))
    target = str(float(docu[M]))
    docu[M] = float(docu[M])
    cnt = 0
    q = deque(docu)
    while True :
        if q[0] == max(q) :
            rel = q.popleft()
            cnt+= 1
            if str(rel) == target :
                break
        else :
            q.append(q.popleft())
    print(cnt)
