n = int(input())
positive = []
negative = []
one = 0
zero = 0

for _ in range(n):
    num = int(input())
    if num > 1:  # 1보다 큰 양수
        positive.append(num)
    elif num == 1:  # 1
        one += 1
    elif num == 0:  # 0
        zero += 1
    else:  # 음수
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

# 양수는 큰 숫자끼리 묶어줌
result = 0
while len(positive) > 1:
    result += positive.pop(0) * positive.pop(0)

# 음수는 작은 숫자끼리 묶어줌
while len(negative) > 1:
    result += negative.pop(0) * negative.pop(0)

# 남은 숫자들을 결과값에 더해줌
result += sum(positive) + sum(negative) + one

# 남은 음수가 있고, 0도 있을 경우, 0과 음수를 곱해서 없앨 수 있음
if negative and zero:
    result -= negative[0]

print(result)