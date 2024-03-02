def count_one(n):
    if n <= 0:
        return 0
    x = len(bin(n)) - 3
    return dp[x] + count_one(n - 2 ** x) + n - 2 ** x + 1

dp = [0] * 55
for i in range(1, 55):
    dp[i] = dp[i-1] * 2 + 2 ** (i - 1)

A, B = map(int, input().split())
print(count_one(B) - count_one(A - 1))
