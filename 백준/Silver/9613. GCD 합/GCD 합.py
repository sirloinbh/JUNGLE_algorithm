def gcd(a,b) :
    if a <= b :
        a,b = b,a
    if a%b == 0 :
        return b
    else :
        return gcd(b,a%b)


T = int(input())
for _ in range(T) :
    n = list(map(int, input().split()))
    gcd_ = 0
    for i in range(1,len(n)) :
        for j in range(i+1, len(n)) :
            gcd_+=gcd(n[i],n[j])
    print(gcd_)