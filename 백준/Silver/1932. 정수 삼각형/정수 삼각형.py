# 삼각형의 크기 N을 입력받습니다.
N = int(input())

# 삼각형의 각 줄에 있는 정수를 입력받습니다.
triangle = [list(map(int, input().split())) for _ in range(N)]

# 각 위치에서의 최대 합을 저장하기 위한 dp 리스트를 초기화합니다.
dp = [[0] * N for _ in range(N)]
dp[0][0] = triangle[0][0]  # 시작 위치의 값을 초기값으로 설정합니다.

# 1번 줄부터 N-1번 줄까지 순차적으로 각 위치에서의 최대 합을 계산합니다.
for i in range(1, N):
    for j in range(i+1):
        # 가장 왼쪽 경계에 위치한 경우와 가장 오른쪽 경계에 위치한 경우는 따로 처리합니다.
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        # 나머지 위치에서는 대각선 왼쪽 위와 대각선 오른쪽 위 중 큰 값을 선택하여 합산합니다.
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

# 마지막 줄에서의 최대 합을 출력합니다.
print(max(dp[N-1]))