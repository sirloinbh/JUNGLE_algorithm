# 꽃의 개수 입력
n = int(input())

# 꽃들의 정보를 저장할 리스트
flowers = []

# 모든 꽃의 정보를 입력 받는다
for _ in range(n):
    a, b, c, d = map(int, input().split())
    start = a * 100 + b  # 시작 날짜
    end = c * 100 + d  # 끝 날짜
    flowers.append((start, end))

# 꽃들을 시작 날짜를 기준으로 정렬한다
flowers.sort()

answer = 0  # 필요한 꽃의 최소 개수
current = 301  # 3월 1일부터 시작
end = 301  # 현재 가장 늦게 지는 꽃의 날짜

idx = 0
while current <= 1130 and idx < n:
    check = False
    while idx < n and flowers[idx][0] <= current:
        if flowers[idx][1] > end:
            end = flowers[idx][1]
            check = True
        idx += 1

    # 만약 더 이상 꽃을 선택할 수 없다면 종료
    if not check:
        answer = 0
        break

    # 꽃을 선택했다면, answer 값을 증가시키고 다음 꽃을 선택하기 위해 current 값을 업데이트한다
    answer += 1
    current = end

# 전체 꽃다발을 만들 수 없는 경우
if current <= 1130:
    print(0)
else:
    print(answer)