import sys
from bisect import bisect_left

# 입력 받기
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()  # A 전봇대를 기준으로 정렬

# LIS 계산을 위한 준비
dp = []  # 실제 LIS 값을 저장 (B 전봇대 번호)
indices = []  # dp 배열에서의 위치를 저장
trace = [-1] * n  # 역추적을 위한 배열

for i, (_, b) in enumerate(lines):
    pos = bisect_left(dp, b)
    if pos == len(dp):
        dp.append(b)
        if dp: indices.append((pos, i))
        if pos > 0: trace[i] = indices[pos-1][1]
    else:
        dp[pos] = b
        indices[pos] = (pos, i)
        if pos > 0: trace[i] = indices[pos-1][1]

# LIS 역추적
lis_set = set()
i = indices[-1][1]
while i != -1:
    lis_set.add(lines[i][0])
    i = trace[i]

# 결과 출력
print(n - len(dp))
for a, _ in lines:
    if a not in lis_set:
        print(a)
