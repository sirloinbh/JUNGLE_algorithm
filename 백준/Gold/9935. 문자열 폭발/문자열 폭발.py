import sys
input = sys.stdin.readline

str1 = input().strip()
bomb = input().strip()

stack = []
bomb_length = len(bomb)

for char in str1:
    stack.append(char)
    if ''.join(stack[-bomb_length:]) == bomb:
        del stack[-bomb_length:]

result = ''.join(stack)
print(result if result else "FRULA")
