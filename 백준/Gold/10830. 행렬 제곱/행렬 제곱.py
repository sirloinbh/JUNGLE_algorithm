import sys
input = sys.stdin.readline

def multiply_matrix(A, B):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def pow_matrix(A, B):
    if B == 1:
        return A
    elif B == 2:
        return multiply_matrix(A, A)
    else:
        temp = pow_matrix(A, B // 2)
        if B % 2 == 0:
            return multiply_matrix(temp, temp)
        else:
            return multiply_matrix(multiply_matrix(temp, temp), A)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = pow_matrix(A, B)

for row in result:
    print(*[n%1000 for n in row])
