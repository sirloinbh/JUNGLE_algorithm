import sys
sys.setrecursionlimit(10**6)

def pre_order(start, end, post_start, post_end):
    if start > end or post_start > post_end:
        return
    root = post_order[post_end]
    print(root, end=' ')

    left = in_order_index[root] - start
    right = end - in_order_index[root]

    pre_order(start, start+left-1, post_start, post_start+left-1)
    pre_order(end-right+1, end, post_end-right, post_end-1)

n = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

in_order_index = [0 for _ in range(n+1)]

for i in range(n):
    in_order_index[in_order[i]] = i

pre_order(0, n-1, 0, n-1)
