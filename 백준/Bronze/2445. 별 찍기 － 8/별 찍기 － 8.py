# 입력: 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
n = int(input())

# 상단 패턴 출력
for i in range(1, n+1):
    # 별을 i개 출력
    print('*' * i, end='')
    # 공백 출력, 각 줄마다 별의 총 개수는 2n이므로 (2n - 2i) 만큼의 공백 출력
    print(' ' * (2*n - 2*i), end='')
    # 오른쪽 별 출력
    print('*' * i)

# 하단 패턴 출력
for i in range(n-1, 0, -1):
    # 별을 i개 출력
    print('*' * i, end='')
    # 공백 출력, 각 줄마다 별의 총 개수는 2n이므로 (2n - 2*i) 만큼의 공백 출력
    print(' ' * (2*n - 2*i), end='')
    # 오른쪽 별 출력
    print('*' * i)