T = int(input())
for _ in range(T) :
    position, string = input().split()
    string = string[:int(position)-1] + string[int(position):]
    print(string)