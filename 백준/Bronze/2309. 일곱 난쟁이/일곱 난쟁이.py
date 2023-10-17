def seven_dwarfs(a) :
    total=sum(a)
    for i in range(9):
        for j in range(i+1,9):
            if total - a[i]-a[j] ==100:
                return sorted(a[:i] + a[i+1:j] + a[j+1:])
    []

a = [int(input()) for _ in range(9)]
for i in seven_dwarfs(a):
    print(i)