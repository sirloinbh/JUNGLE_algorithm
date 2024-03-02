import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    array = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    done = [0] * (n + 1)

    count = 0
    for i in range(1, n + 1):
        if visited[i] == 0:
            start = i
            stack = [start]
            visited[start] = 1

            # DFS
            while stack:
                cur_node = stack[-1]
                next_node = array[cur_node]
                if visited[next_node] == 0:
                    stack.append(next_node)
                    visited[next_node] = 1
                elif visited[next_node] == 1 and done[next_node] == 0:
                    count += len(stack) - stack.index(next_node)
                    while stack:
                        done[stack.pop()] = 1
                elif visited[next_node] == 1 and done[next_node] == 1:
                    while stack:
                        done[stack.pop()] = 1
            
    print(n - count)
