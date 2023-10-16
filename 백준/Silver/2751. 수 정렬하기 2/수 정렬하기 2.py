import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

for num in sorted(numbers):
    print(num)