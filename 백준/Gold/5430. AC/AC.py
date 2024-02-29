from collections import deque
import sys

def AC(com, arr):
    com = deque(com)
    arr = deque(arr)
    R = False

    while com:
        c = com.popleft()
        if c == 'R':
            R = not R
        elif c == 'D':
            if arr:
                if R:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                return 'error'
    return list(arr) if not R else list(reversed(arr))

T = int(sys.stdin.readline())

for _ in range(T):
    com = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')
    if arr[0] != '':
        arr = list(map(int, arr))
    else:
        arr = []
    result = AC(com, arr)
    if result == 'error':
        print(result)
    else:
        print('[' + ','.join(map(str, result)) + ']')
