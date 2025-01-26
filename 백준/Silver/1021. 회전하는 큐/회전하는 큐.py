import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    N = int(input[0])  # 큐의 크기
    M = int(input[1])  # 뽑아내려는 숫자의 개수
    targets = list(map(int, input[2:2+M]))  # 뽑아내려는 숫자들

    dq = deque(range(1, N+1))  # 덱 초기화
    total_operations = 0  # 총 회전 횟수

    for target in targets:
        idx = dq.index(target)  # 현재 뽑아야 할 숫자의 인덱스
        if idx <= len(dq) // 2:
            # 왼쪽으로 회전
            dq.rotate(-idx)
            total_operations += idx
        else:
            # 오른쪽으로 회전
            rotations = len(dq) - idx
            dq.rotate(rotations)
            total_operations += rotations
        dq.popleft()  # 첫 번째 원소 제거

    print(total_operations)

if __name__ == "__main__":
    main()
