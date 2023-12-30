odds = []

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        odds.append(n)
if not odds:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))