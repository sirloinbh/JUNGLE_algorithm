import sys

class Queue:
    def __init__(self):
        self.items = []
        
    def push(self, x):
        self.items.append(x)
        
    def pop(self):
        if self.items :
            t = self.items[0]
            self.items.remove(self.items[0])
            return t
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
queue = Queue() 

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        queue.push(int(command[1]))
    elif command[0] == "pop":
        print(queue.pop())
    elif command[0] == "size":
        print(queue.size())
    elif command[0] == "empty":
        print(queue.empty())
    elif command[0] == "front":
        print(queue.front())
    elif command[0] == "back":
        print(queue.back())