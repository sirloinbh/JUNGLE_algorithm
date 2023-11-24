n = int(input())  # 회의의 개수

# 회의의 시작 시간과 끝나는 시간 입력 받기
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 회의를 끝나는 시간을 기준으로 정렬하고, 동일한 경우 시작 시간으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

end_time = 0  # 이전에 선택된 회의의 끝나는 시간
count = 0  # 선택된 회의의 수

for start, end in meetings:
    # 현재 회의의 시작 시간이 이전 회의의 끝나는 시간 이후라면 회의를 선택
    if start >= end_time:
        count += 1
        end_time = end

print(count)