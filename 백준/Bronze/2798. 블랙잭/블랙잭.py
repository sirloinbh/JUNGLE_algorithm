N, M = map(int, input().split())
cards = list(map(int, input().split()))
maximum = 0
for i in range(len(cards)) :
    for j in range(i+1, len(cards)) :
        for k in range(j+1, len(cards)) :
            if cards[i] + cards[j] +cards[k] <= M :
                maximum = max(maximum, cards[i] + cards[j] +cards[k])
print(maximum)