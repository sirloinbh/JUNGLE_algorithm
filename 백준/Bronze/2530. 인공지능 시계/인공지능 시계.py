H,M,S  = map(int, input().split())
A = int(input())
H = (H +(M + A//60 + (S + A%60) // 60) // 60)%24
M = (M + A//60 + (S + A%60) // 60) % 60
S = (S + A%60) % 60

print(H,M,S)