N= int(input())

for i in range(1,N+1):
  a,b =map(int,input().split())
  c=a+b

  print("Case #%d: %d + %d = %d" %(i,a,b,c))