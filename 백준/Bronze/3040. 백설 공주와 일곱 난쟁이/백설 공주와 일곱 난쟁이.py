dwarf = [int(input()) for _ in range(9)]
for i in range(8) :
    for j in range(i+1,9) :
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100 :
            a=dwarf[i]
            b=dwarf[j]

dwarf.remove(a)
dwarf.remove(b)
            

for k in range(len(dwarf)):
    print(dwarf[k])
