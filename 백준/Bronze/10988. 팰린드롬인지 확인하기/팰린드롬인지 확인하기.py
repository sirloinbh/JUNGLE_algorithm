word=str(input())
cnt=1
for i in range(len(word)//2+1) :
    if word[i]!=word[len(word)-i-1] :
        cnt=0
        break
    
print(cnt)