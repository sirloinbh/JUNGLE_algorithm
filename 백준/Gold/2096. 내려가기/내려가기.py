import sys
input = sys.stdin.readline

N = int(input())
max_dp = [0] * 3
min_dp = [0] * 3
max_temp = [0] * 3
min_temp = [0] * 3

for _ in range(N):
    row = list(map(int, input().split()))
    max_temp[0] = max(max_dp[0], max_dp[1]) + row[0]
    max_temp[1] = max(max_dp) + row[1]
    max_temp[2] = max(max_dp[1], max_dp[2]) + row[2]
    min_temp[0] = min(min_dp[0], min_dp[1]) + row[0]
    min_temp[1] = min(min_dp) + row[1]
    min_temp[2] = min(min_dp[1], min_dp[2]) + row[2]
    max_dp, min_dp = max_temp[:], min_temp[:]

print(max(max_dp), min(min_dp))
