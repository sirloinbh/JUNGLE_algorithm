from itertools import combinations  # 조합을 생성하기 위해 필요한 모듈

while True:
    data = list(map(int, input().split()))  # 데이터 입력
    if data[0] == 0:  # 0이 첫 번째로 들어오면 입력 종료
        break

    k = data[0]  # k값(데이터의 개수)
    nums = data[1:]  # 실제 로또 번호 후보들

    # itertools의 combinations 함수를 사용하여 6개를 선택하는 모든 조합 생성
    for comb in combinations(nums, 6):
        print(' '.join(map(str, comb)))  # 조합 출력
    print()  # 각 테스트 케이스 사이에는 공백 한 줄 출력