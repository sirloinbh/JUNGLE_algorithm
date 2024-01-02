N = input()
list_ = []
for char in N :
    list_.append(int(char))
if '0' not in N :
    print(-1)
elif sum(list_)%3 != 0 :
    print(-1)
else :
    list_.sort(reverse=True)
    for i in list_ :
        print(i, end='')