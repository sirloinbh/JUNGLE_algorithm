import sys
sys.setrecursionlimit(10**6)

def energy(a, b):
    if a == b:
        return 1
    elif a == 0 or b == 0:
        return 2
    elif abs(a-b) == 2:
        return 4
    else:
        return 3

def ddr(left, right, index):
    if index == len(steps):
        return 0
    if dp[left][right][index] != -1:
        return dp[left][right][index]
    next_step = steps[index]
    dp[left][right][index] = min(ddr(next_step, right, index+1) + energy(left, next_step), ddr(left, next_step, index+1) + energy(right, next_step))
    return dp[left][right][index]

steps = list(map(int, sys.stdin.readline().split()))
steps.pop()
dp = [[[-1]*len(steps) for _ in range(5)] for _ in range(5)]
print(ddr(0, 0, 0))
