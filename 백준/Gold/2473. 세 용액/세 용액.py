import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

min_value = float('inf')
answer = []

for i in range(n-2):
    left, right = i+1, n-1
    while left < right:
        temp = liquid[i] + liquid[left] + liquid[right]
        if abs(temp) < min_value:
            min_value = abs(temp)
            answer = [liquid[i], liquid[left], liquid[right]]
        if temp < 0:
            left += 1
        else:
            right -= 1

print(*answer)
