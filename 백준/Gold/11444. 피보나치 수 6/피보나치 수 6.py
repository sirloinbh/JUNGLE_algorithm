import sys
input = sys.stdin.readline

def multiply_matrix(A, B):
    result = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000000007
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

N = int(input())
A = [[1, 1], [1, 0]]

if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    result = pow_matrix(A, N-1)[0][0]
    print(result)
