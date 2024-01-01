T = int(input())
for _ in range(T) :
    even = []
    nums = list(map(int, input().split()))
    for num in nums :
        if num %2 == 0 :
            even.append(num)
    print(sum(even), min(even))