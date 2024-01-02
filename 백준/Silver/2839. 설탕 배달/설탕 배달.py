N = int(input())
mini = 100000
for i in range(1001) :
    for j in range(2001) :
        if 5*i+3*j == N :
            mini = min(mini, i+j)
if mini == 100000 :
    print(-1)
else :
    print(mini)