import sys
n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(sys.stdin.readline().strip())


def quard_zip(arr, x, y, N):
    base_num = arr[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if base_num != arr[i][j]:
                print("(", end="")
                quard_zip(arr, x, y, N // 2)
                quard_zip(arr, x, y + N // 2, N // 2)
                quard_zip(arr, x + N // 2, y, N // 2)
                quard_zip(arr, x + N // 2, y + N // 2, N // 2)
                print(")", end="")
                return
    print(base_num, end="")

quard_zip(n_list, 0, 0, n)