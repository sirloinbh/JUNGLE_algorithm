import sys

N = int(sys.stdin.readline())
words = set()  # set을 사용하여 중복된 단어를 제거

for _ in range(N):
    words.add(sys.stdin.readline().strip())

# 단어들을 길이와 사전 순으로 정렬
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)