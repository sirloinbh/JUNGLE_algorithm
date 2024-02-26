N = int(input())
zero_num = 0

# 5의 거듭제곱으로 나누기
power_of_5 = 5
while N >= power_of_5:
    zero_num += N // power_of_5
    power_of_5 *= 5

print(zero_num)
