button1 = [300, 60, 10]
button2 = [0, 0, 0]
T = int(input())

for i in range(3) :
    button2[i] += T//button1[i]
    T = T%button1[i]

if T>0 : 
    print(-1)
else : 
    print(*button2)
