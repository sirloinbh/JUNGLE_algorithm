# N 입력받기
N=int(input())

# 사이클 카운트 세기
cnt=0

#숫자를 바뀌게 하는 변수 도입
M=N

#M 변수 한사이클 돌리기
if M<10 :
    M=M*10+M
    cnt+=1
else :
    M=(M%10)*10+((M//10)+M%10)%10
    cnt+=1
    
#M==N이 될 때까지 사이클 돌리기
while M!=N:
    if M<10 :
        M=M*10+M
        cnt+=1
    else :
        M=(M%10)*10+((M//10)+M%10)%10
        cnt+=1

#사이클 수 출력
print(cnt)

