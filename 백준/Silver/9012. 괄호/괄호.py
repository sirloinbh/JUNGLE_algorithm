T = int(input())
for _ in range(T) :
    stack = []
    data = input()
    for char in data :
        if char == '(' :
            stack.append(char)
        elif char ==')' :
            if len(stack) == 0 :
                stack.append(char)
            elif stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(char)
    if len(stack) :
        print("NO")
    else :
        print("YES")