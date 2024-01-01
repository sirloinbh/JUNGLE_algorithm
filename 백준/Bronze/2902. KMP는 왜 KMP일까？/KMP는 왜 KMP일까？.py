Names = input()
Names_split = Names.split('-')
KMP = []
for name in Names_split :
    KMP.append(name[:1])
    
print(''.join(KMP))