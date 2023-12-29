T = int(input())
for _ in range(T) :
    A,Grade = 0,0
    N = int(input())
    for _ in range(N) :
        C, G = map(float, input().split())
        A += C
        Grade += C*G
    GPA = (Grade/A)
    print(int(A),f"{GPA:.1f}")