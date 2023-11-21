# 극장의 좌석 수 N과 VIP 회원의 수 M을 입력 받습니다.
N = int(input())
M = int(input())

# VIP 회원의 좌석 번호를 저장합니다.
VIPs = [int(input()) for _ in range(M)]

# dp[i]: i개의 연속된 좌석에서 자리를 바꿀 수 있는 경우의 수
dp = [1, 1, 2] + [0] * (N-2)

# dp 배열을 채웁니다. 3번째 좌석부터 i번째 좌석까지의 경우의 수는 i-1번째와 i-2번째의 합이 됩니다.
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

# 결과를 저장할 변수입니다. 초기값은 1입니다.
result = 1

# 첫 번째 VIP 좌석 앞의 좌석 수를 구합니다.
start = 0
for vip in VIPs:
    end = vip - 1  # VIP 좌석 앞에 있는 좌석의 번호
    result *= dp[end-start]  # end와 start 사이의 좌석에서 자리를 바꿀 수 있는 경우의 수를 곱합니다.
    start = vip  # 다음 구간의 시작 좌석 번호를 갱신합니다.

# 마지막 VIP 좌석 뒤의 좌석 수를 고려합니다.
result *= dp[N-start]

# 결과를 출력합니다.
print(result)