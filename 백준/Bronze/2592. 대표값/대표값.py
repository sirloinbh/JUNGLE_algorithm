sum_ = 0
freq = []
freq_ = 0
max_ = 0
for _ in range(10) :
    n = int(input())
    sum_+=n
    freq.append(n)

for i in freq :
    max_ = max(max_,freq.count(i))
    if max_ == freq.count(i) :
        freq_ = i
    

print(sum_//10)
print(freq_)
