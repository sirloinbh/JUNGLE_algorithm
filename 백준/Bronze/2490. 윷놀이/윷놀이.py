result = ["D", "C", "B", "A", "E"]

for _ in range(3):
    yut = list(map(int, input().split()))
    count = yut.count(1)
    print(result[count])