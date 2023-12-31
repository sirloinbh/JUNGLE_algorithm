appliance = [0]
score = [0]
win_score = 0
for i in range(1,6) :
    scores = map(int, input().split())
    appliance.append(i)
    score.append(sum(scores))
    

for i in range(1,6) :
    if score[i] == max(score) :
        print(appliance[i], score[i])