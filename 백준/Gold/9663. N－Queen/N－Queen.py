def solve(row, left, right, vertical):
    global result
    available = ((1 << N) - 1) & ~(left | right | vertical)
    while available:
        lsb = -available & available
        available -= lsb
        if row == N - 1:
            result += 1
        else:
            solve(row + 1, (left | lsb) << 1, (right | lsb) >> 1, vertical | lsb)

N = int(input())
result = 0
solve(0, 0, 0, 0)
print(result)
