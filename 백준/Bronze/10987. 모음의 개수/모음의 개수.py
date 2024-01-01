word = input()
moeum = "aeiou"
cnt = 0
for char in moeum :
    cnt += word.count(char)
print(cnt)