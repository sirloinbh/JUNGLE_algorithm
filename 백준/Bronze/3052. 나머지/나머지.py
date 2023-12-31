a=list(int(input()) for _ in range(10))
rest = []
for i in a:
    if i%42 not in rest :
        rest.append(i%42)

print(len(rest))