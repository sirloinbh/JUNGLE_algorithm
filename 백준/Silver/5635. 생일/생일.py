n = int(input())
mydic = {}
for _ in range(n) :
    name, day, month, year = input().split()
    day = int(day) + int(month)*31 + int(year)*12*31
    mydic[name] = day

print(max(mydic, key=mydic.get))
print(min(mydic, key=mydic.get))
