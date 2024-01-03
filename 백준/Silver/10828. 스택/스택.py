import sys

# Stack 클래스를 정의하여 스택의 기본 연산들을 구현합니다.
class Stack:
    # 초기화 메서드에서 스택을 빈 리스트로 초기화합니다.
    def __init__(self):
        self.items = []
        
    # push 메서드: 스택의 맨 위에 값을 추가합니다.
    def push(self, x):
        self.items.append(x)
        
    # pop 메서드: 스택의 맨 위 값을 제거하고 반환합니다. 스택이 비어있는 경우 -1을 반환합니다.
    def pop(self):
        return self.items.pop() if self.items else -1
    
    # size 메서드: 스택에 들어있는 값의 수를 반환합니다.
    def size(self):
        return len(self.items)
    
    # empty 메서드: 스택이 비어있는지 확인합니다. 비어있다면 1을, 그렇지 않다면 0을 반환합니다.
    def empty(self):
        return 1 if not self.items else 0
    
    # top 메서드: 스택의 맨 위 값을 반환합니다. 스택이 비어있는 경우 -1을 반환합니다.
    def top(self):
        return self.items[-1] if self.items else -1

# 사용자로부터 스택 연산의 수 n을 입력 받습니다.
n = int(input())
stack = Stack()  # Stack 클래스의 인스턴스를 생성합니다.

# n번의 연산을 처리하기 위한 반복문입니다.
for _ in range(n):
    # 연산을 문자열로 입력 받습니다. sys.stdin.readline()은 입력 속도를 빠르게 하기 위한 메서드입니다.
    command = sys.stdin.readline().split()

    # 입력받은 연산에 따라 스택의 메서드를 호출하고 결과를 출력합니다.
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())