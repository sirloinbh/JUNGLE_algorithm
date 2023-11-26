import sys

# 입력: 선분의 개수 N
N = int(sys.stdin.readline())

# 각 선분의 시작점과 끝점을 입력 받아 저장
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 선분을 시작점을 기준으로 오름차순 정렬
lines.sort(key=lambda x: x[0])

# result: 합쳐진 선분들의 총 길이
result = 0

# start, end: 현재 참고하고 있는 선분의 시작점과 끝점
# 초기값은 문제에서 주어진 범위 밖의 값을 사용
start, end = -1000000001, -1000000001

# 모든 선분에 대하여
for line in lines:
    # 현재 선분의 시작점이 이전 선분의 끝점보다 클 경우
    # (선분이 겹치지 않는 경우)
    if end < line[0]:
        # 이전까지의 합쳐진 선분의 길이를 결과에 더함
        result += end - start
        # 현재 선분을 새로운 선분으로 설정
        start, end = line[0], line[1]
    # 선분이 겹치는 경우
    else:
        # 겹치는 선분들 중 가장 큰 끝점으로 갱신
        end = max(end, line[1])

# 마지막으로 참고하고 있던 선분의 길이를 결과에 더함
result += end - start

print(result)