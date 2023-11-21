T = int(input())  # 테스트 케이스의 개수

for _ in range(T):
    n = int(input())  # 스티커의 열의 수
    stickers = [list(map(int, input().split())) for _ in range(2)]

    # 스티커가 1열일 때는 그냥 해당 위치의 스티커 값이 최댓값이다.
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    # 초기 dp 테이블 설정
    stickers[0][1] += stickers[1][0]
    stickers[1][1] += stickers[0][0]

    # 각 위치에서의 최댓값 계산
    for j in range(2, n):
        stickers[0][j] += max(stickers[1][j-1], stickers[1][j-2])
        stickers[1][j] += max(stickers[0][j-1], stickers[0][j-2])

    # 최종 결과 출력
    print(max(stickers[0][-1], stickers[1][-1]))