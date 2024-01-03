import sys

class Deque:
    def __init__(self):
        self.items = []
        
    def push_front(self, x):
        self.items = [x]+self.items
        
    def push_back(self, x):
        self.items.append(x)
        
    def pop_front(self):
        if self.items :
            t = self.items[0]
            self.items.remove(self.items[0])
            return t
        else :
            return -1
        
    def pop_back(self):
        if self.items :
            return self.items.pop()
        else :
            return -1
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return 1 if not self.items else 0
    
    def front(self):
        return self.items[0] if self.items else -1
    
    def back(self):
        return self.items[-1] if self.items else -1

n = int(input())
deque = Deque() 

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == "push_back":
        deque.push_back(int(command[1]))
    elif command[0] == "push_front":
        deque.push_front(int(command[1]))
    elif command[0] == "pop_back":
        print(deque.pop_back())
    elif command[0] == "pop_front":
        print(deque.pop_front())
    elif command[0] == "size":
        print(deque.size())
    elif command[0] == "empty":
        print(deque.empty())
    elif command[0] == "front":
        print(deque.front())
    elif command[0] == "back":
        print(deque.back())