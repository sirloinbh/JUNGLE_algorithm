# 사람의 수 입력 받기
n = int(input())

# 각 사람이 돈을 인출하는데 걸리는 시간을 입력 받아 오름차순으로 정렬한다.
times = list(map(int, input().split()))
times.sort()

# 이전 사람까지의 누적 시간을 저장하는 변수
prev_time = 0
# 모든 사람이 인출하는데 걸리는 총 시간
total_time = 0

# 각 사람에 대하여
for time in times:
    # 현재 사람이 인출하는데 걸리는 시간은 이전 사람까지의 누적 시간 + 현재 사람의 시간
    current_time = prev_time + time
    # 총 시간에 현재 사람이 인출하는데 걸리는 시간을 더한다.
    total_time += current_time
    # 이전 사람까지의 누적 시간 업데이트
    prev_time = current_time

print(total_time)