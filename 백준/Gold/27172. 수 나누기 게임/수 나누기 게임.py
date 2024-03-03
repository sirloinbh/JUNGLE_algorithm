import sys

N = int(sys.stdin.readline().strip())

# Flag array to check the presence of numbers
chk = [False] * 1000001
# Array to hold the final scores
result = [0] * 1000001

# Reading the card numbers
nums = list(map(int, sys.stdin.readline().split()))

# Marking the presence of card numbers
for num in nums:
    chk[num] = True

# Sorting the numbers to efficiently find multiples
for num in sorted(nums):
    # Incrementing scores for divisors and decrementing for multiples
    for j in range(num * 2, 1000001, num):
        if chk[j]:
            result[num] += 1
            result[j] -= 1

# Printing the final scores
for num in nums:
    print(result[num], end=' ')
