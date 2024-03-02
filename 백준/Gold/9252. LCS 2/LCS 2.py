import sys
input = sys.stdin.readline

str1 = ' ' + input().strip()
str2 = ' ' + input().strip()

dp = [[0]*(len(str2)) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])

# 역추적하여 최장 공통 부분 수열 찾기
LCS = ''
i = len(str1) - 1
j = len(str2) - 1
while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        LCS = str1[i] + LCS
        i -= 1
        j -= 1

print(LCS)
