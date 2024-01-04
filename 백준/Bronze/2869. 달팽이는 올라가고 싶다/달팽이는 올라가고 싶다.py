A, B, V = map(int, input().split())
if (V-A)%(A-B) :
    snail = (V-A)//(A-B)+2
else :
    snail = (V-A)//(A-B)+1
print(snail)