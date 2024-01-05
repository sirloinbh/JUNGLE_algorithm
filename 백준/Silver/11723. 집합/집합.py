import sys
set_ = set([])
N = int(sys.stdin.readline())
for _ in range(N) :
    purpose = list(map(str, sys.stdin.readline().split()))
    if purpose[0] == 'add' :
        set_.add(purpose[1])
    elif purpose[0] == 'remove' :
        if purpose[1] in set_ :
            set_.remove(purpose[1])
    elif purpose[0] == 'remove' :
        if purpose[1] in set_ :
            set_.remove(purpose[1])
    elif purpose[0] == 'check' :
        if purpose[1] in set_ :
            print(1)
        else :
            print(0)
    elif purpose[0] == 'toggle' :
        if purpose[1] in set_ :
            set_.remove(purpose[1])
        else :
            set_.add(purpose[1])
    elif purpose[0] == 'all' :
        set_ = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif purpose[0] == 'empty' :
        set_.clear()
