L = int(input())
string = input()
sum = 0
i=0
for char in string :
    sum += (ord(char)-96)*(31**i)
    i+=1
print(sum%1234567891)