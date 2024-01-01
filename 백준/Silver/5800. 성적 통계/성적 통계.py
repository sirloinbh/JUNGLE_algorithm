T = int(input())
for i in range(1,T+1) :
    math_gap = []
    math_ = list(map(int, input().split()))
    math_score = math_[1:]
    math_score.sort()
    for j in range(len(math_score)-1) :
        math_gap.append(math_score[j+1]-math_score[j])
    print(f"Class {i}")
    print(f"Max {max(math_score)}, Min {min(math_score)}, Largest gap {max(math_gap)}")
    