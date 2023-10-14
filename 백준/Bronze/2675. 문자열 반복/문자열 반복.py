for _ in range(int(input())) :
    cnt=""
    R,S=input().split()
    for i in S :
        cnt+=int(R)*i
    print(cnt)