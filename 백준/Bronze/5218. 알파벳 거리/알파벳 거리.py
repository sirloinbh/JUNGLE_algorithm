T = int(input())
alphabet = {"A":1, "B":2, "C":3, "D":4, "E":5,
            "F":6, "G":7, "H":8, "I":9, "J":10,
            "K":11,"L":12,"M":13,"N":14,"O":15,
            "P":16,"Q":17,"R":18,"S":19,"T":20,
            "U":21,"V":22,"W":23,"X":24,"Y":25,
            "Z":26}
for _ in range(T) :
    word_list1 = []
    word_list2 = []
    distance = []
    word1, word2 = map(str,input().split())
    for char in word1:
        word_list1.append(alphabet[char])
    for char in word2:
        word_list2.append(alphabet[char])
    for i in range(len(word_list1)) :
        if word_list1[i]>word_list2[i] :
            distance.append(word_list2[i]-word_list1[i]+26)
        else :
            distance.append(word_list2[i]-word_list1[i])
    print("Distances:",*distance)