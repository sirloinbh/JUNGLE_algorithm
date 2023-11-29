from itertools import combinations

# 입력 받기
L, C = map(int, input().split())
chars = list(input().split())

# 정렬
chars.sort()

# 모음 리스트
vowels = ['a', 'e', 'i', 'o', 'u']

# 조합을 이용해 가능한 암호 후보 생성
for password in combinations(chars, L):
    # 모음, 자음 개수 확인
    count_vowels = sum(1 for char in password if char in vowels)
    count_consonants = L - count_vowels

    # 조건에 부합하는 암호만 출력
    if count_vowels >= 1 and count_consonants >= 2:
        print(''.join(password))