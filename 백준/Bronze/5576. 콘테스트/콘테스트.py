score = [int(input()) for _ in range(20)]
W_score = sorted(score[:10])
K_score = sorted(score[10:])
print(sum(W_score[-3:]), sum(K_score[-3:]))