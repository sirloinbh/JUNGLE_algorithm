T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        item, category = input().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1

    result = 1
    for key in clothes.keys():
        result *= (clothes[key] + 1)

    print(result - 1)
