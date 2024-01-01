zero_num = 0

N = int(input())
for i in range(1,N+1) :
    if i%125 == 0 :
        zero_num += 3
    elif i%25 == 0 :
        zero_num += 2
    elif i%5 == 0 :
        zero_num += 1
print(zero_num)