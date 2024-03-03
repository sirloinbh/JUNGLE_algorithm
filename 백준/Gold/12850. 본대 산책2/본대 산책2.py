def matrix_mul(A, B, mod):
    # 행렬 곱셈 함수
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= mod
    return result

def matrix_pow(matrix, power, mod):
    # 행렬 거듭제곱 함수 (분할 정복 방법 사용)
    size = len(matrix)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        result[i][i] = 1
    while power > 0:
        if power % 2 == 1:
            result = matrix_mul(result, matrix, mod)
        matrix = matrix_mul(matrix, matrix, mod)
        power //= 2
    return result

# 문제에서 주어진 그래프의 인접 행렬
adj_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0], # 정보과학관
    [1, 0, 1, 1, 0, 0, 0, 0], # 전산관
    [1, 1, 0, 1, 1, 0, 0, 0], # 미래관
    [0, 1, 1, 0, 1, 1, 0, 0], # 신양관
    [0, 0, 1, 1, 0, 1, 0, 1], # 한경직기념관
    [0, 0, 0, 1, 1, 0, 1, 0], # 진리관
    [0, 0, 0, 0, 0, 1, 0, 1], # 학생회관
    [0, 0, 0, 0, 1, 0, 1, 0]  # 형남공학관
]
mod = 1000000007

# D 입력 받기
D = int(input())

# D분 후의 건물별 도달 가능 경로 수 계산
result_matrix = matrix_pow(adj_matrix, D, mod)

# 정보과학관으로 돌아올 수 있는 경로의 수 출력
print(result_matrix[0][0])
