from collections import deque

def D(n):
    return (2 * n) % 10000

def S(n):
    return (n - 1) % 10000 if n > 0 else 9999

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10

def BFS(A, B):
    visited = [False] * 10000
    queue = deque([(A, "")])
    visited[A] = True

    while queue:
        current, commands = queue.popleft()
        if current == B:
            return commands

        for command, func in [('D', D), ('S', S), ('L', L), ('R', R)]:
            next_state = func(current)
            if not visited[next_state]:
                visited[next_state] = True
                queue.append((next_state, commands + command))

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    result = BFS(A, B)
    print(result)
