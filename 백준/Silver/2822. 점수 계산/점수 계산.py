mydic = {}

for i in range(1,9) :
    mydic[i] = int(input())

for _ in range(3) :
    min_value = min(mydic.values())
    for key, value in mydic.items() :
        if value == min_value :
            min_key = key
    del mydic[min_key]
print(sum(mydic.values()))
print(*(mydic.keys()))