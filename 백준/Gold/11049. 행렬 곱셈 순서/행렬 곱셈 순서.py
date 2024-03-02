n = int(input())  # 행렬의 개수
matrix_sizes = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]  # DP 테이블 초기화

for length in range(1, n):  # 부분 문제의 크기(곱셈을 수행할 행렬의 개수 - 1)
    for i in range(n - length):  # 시작 행렬의 인덱스
        j = i + length  # 끝 행렬의 인덱스
        dp[i][j] = float('inf')  # 최소값을 찾기 위해 초기값을 무한대로 설정
        for k in range(i, j):  # 분할 위치
            cost = dp[i][k] + dp[k+1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])
