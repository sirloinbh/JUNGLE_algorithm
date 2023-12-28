N = int(input())
yonsei_score,korea_score = 0,0

for _ in range(N) :
    for i in range(9) :
        y_score,k_score = map(int, input().split())
        yonsei_score += y_score
        korea_score += k_score
    
    if yonsei_score > korea_score :
        print("Yonsei")
    elif yonsei_score < korea_score :
        print("Korea")
    else :
        print("Draw")