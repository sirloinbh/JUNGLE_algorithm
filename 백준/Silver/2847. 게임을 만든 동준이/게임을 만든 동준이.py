n = int(input())
scores = [int(input()) for _ in range(n)]

count = 0
# 끝에서부터 시작해서 첫 번째 원소까지 검사
for i in range(n-1, 0, -1):
    # 앞 레벨 점수가 현재 레벨 점수보다 크거나 같다면 조절
    while scores[i-1] >= scores[i]:
        scores[i-1] -= 1
        count += 1

print(count)