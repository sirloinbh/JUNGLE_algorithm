while True :
    stack = []
    string = input()
    if string == '.' :
        break
    else :
        for char in string :
            if char == '(' or char == '[':
                stack.append(char)
            elif char == ')' :
                if stack and stack[-1] == '(' :
                    stack.pop()
                else : 
                    stack.append(char)
            elif char == ']' :
                if stack and stack[-1] == '[' :
                    stack.pop()
                else : 
                    stack.append(char)
    if stack :
        print("no")
    else :
        print("yes")