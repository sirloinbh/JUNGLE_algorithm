import math
import sys
from collections import Counter
def round_(n) :
    if n>=0 :
        return math.floor(n+0.5)
    else :
        return math.ceil(n-0.5)
    
def ari(nums) :
    return round_(sum(nums)/len(nums))

def mid(nums) :
    nums.sort()
    return nums[int(len(nums)/2)]

def fre(nums) :
    nums = Counter(nums)
    fre_ = []
    for key in nums.keys() :
        if nums[key] == max(nums.values()) :
            fre_.append(key)
    fre_.sort()
    if len(fre_) == 1 :
        return fre_[0]
    else :
        return fre_[1]
def ran(nums) :
    return max(nums)-min(nums)


N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(N)]

print(ari(nums))
print(mid(nums))
print(fre(nums))
print(ran(nums))
