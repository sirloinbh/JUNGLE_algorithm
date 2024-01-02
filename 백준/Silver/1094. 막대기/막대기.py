X = int(input())
m = [64]
while sum(m) > X :
    short = m.pop()
    if sum(m) + short//2 >= X :
        m.append(short//2)
    else :
        m.append(short//2)
        m.append(short//2)

print(len(m))