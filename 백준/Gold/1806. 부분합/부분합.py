import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
_sum = 0
min_length = float('inf')

while True:
    if _sum >= S:
        min_length = min(min_length, end - start)
        _sum -= arr[start]
        start += 1
    elif end == N:
        break
    else:
        _sum += arr[end]
        end += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)
