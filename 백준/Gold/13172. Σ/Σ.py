import sys
input = sys.stdin.readline

def power(a, b):
    if b == 1:
        return a % MOD
    else:
        temp = power(a, b // 2)
        if b % 2 == 0:
            return temp * temp % MOD
        else:
            return temp * temp * a % MOD
            
MOD = 10**9+7
M = int(input())
result = 0
for _ in range(M):
    N, S = map(int, input().split())
    result = (result + S * power(N, MOD - 2)) % MOD
print(result)
