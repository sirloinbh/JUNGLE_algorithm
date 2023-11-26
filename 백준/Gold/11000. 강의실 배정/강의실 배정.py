import heapq
import sys

N = int(sys.stdin.readline())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
classes.sort(key=lambda x: x[0])  # 시작 시간을 기준으로 정렬

rooms = []  # 각 강의실의 마지막 수업의 종료 시간을 저장할 힙
heapq.heappush(rooms, classes[0][1])  # 첫 번째 수업의 종료 시간을 힙에 추가

for i in range(1, N):
    if rooms[0] <= classes[i][0]:  # 가장 빨리 끝나는 강의실의 마지막 수업이 현재 수업 시작 전에 끝나면
        heapq.heappop(rooms)  # 해당 강의실에서 현재 수업을 진행

    heapq.heappush(rooms, classes[i][1])  # 현재 수업의 종료 시간을 힙에 추가

print(len(rooms))  # 필요한 강의실의 수 출력