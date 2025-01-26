import sys
import math

def input():
    return sys.stdin.readline()

def is_square(num):
    if num < 0:
        return False
    root = int(math.isqrt(num))
    return root * root == num

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(N)]
    max_square = -1

    for i in range(N):
        for j in range(M):
            for dx in range(-N, N):
                for dy in range(-M, M):
                    if dx == 0 and dy == 0:
                        continue
                    num = ''
                    x, y = i, j
                    while 0 <= x < N and 0 <= y < M:
                        num += grid[x][y]
                        number = int(num)
                        if is_square(number):
                            if number > max_square:
                                max_square = number
                        x += dx
                        y += dy

    print(max_square)

if __name__ == "__main__":
    main()
