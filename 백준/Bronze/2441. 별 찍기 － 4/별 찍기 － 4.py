# 입력: 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
n = int(input())

# 출력: 첫째 줄부터 N번째 줄까지 차례로 별을 출력한다.
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * i)