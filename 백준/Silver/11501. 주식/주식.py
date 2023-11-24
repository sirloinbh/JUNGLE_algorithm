T = int(input())  # 테스트 케이스 수

for _ in range(T):
    N = int(input())  # 주식 가격을 알려주는 날의 수
    prices = list(map(int, input().split()))  # 각 날의 주식 가격

    # 마지막 날의 주식 가격이 최대 주식 가격이 될 것임
    max_price = prices[-1]

    # 이익을 저장할 변수
    profit = 0

    # 주식 가격을 뒤에서부터 순회
    for i in range(N - 2, -1, -1):  # 마지막 날부터 첫 날까지 거꾸로 순회
        if prices[i] < max_price:  # 현재 날의 주식 가격이 이후의 최대 주식 가격보다 작으면
            profit += max_price - prices[i]  # 이익에 차이만큼 더함
        else:  # 현재 날의 주식 가격이 이후의 최대 주식 가격보다 크거나 같으면
            max_price = prices[i]  # 최대 주식 가격 갱신

    print(profit)  # 이익 출력