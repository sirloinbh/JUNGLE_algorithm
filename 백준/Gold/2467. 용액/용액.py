import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left, right = 0, N-1
answer = liquid[left] + liquid[right]
answer_pair = (liquid[left], liquid[right])

while left < right:
    temp = liquid[left] + liquid[right]
    if abs(temp) < abs(answer):
        answer = temp
        answer_pair = (liquid[left], liquid[right])
        if answer == 0:
            break
    if temp < 0:
        left += 1
    else:
        right -= 1

print(answer_pair[0], answer_pair[1])
