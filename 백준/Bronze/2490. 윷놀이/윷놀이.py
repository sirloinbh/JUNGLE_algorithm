
# 윷놀이 결과를 문자열 리스트로 표현
result = ["D", "C", "B", "A", "E"]

# 3번의 윷놀이를 진행하므로 3번 반복
for _ in range(3):
    # 윷의 결과를 입력받는다.
    yut = list(map(int, input().split()))

    # 등(1)의 개수를 카운트
    count = yut.count(1)

    # 결과를 출력
    print(result[count])