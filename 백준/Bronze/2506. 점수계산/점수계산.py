N = int(input())
num = list(map(int, input().split()))
score , total_score = 0,0
for i in range(len(num)) :
    if num[i] : score += 1
    else : score = 0
    total_score += score
print(total_score)