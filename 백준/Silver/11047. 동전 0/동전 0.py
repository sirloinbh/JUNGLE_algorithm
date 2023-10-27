# 동전의 종류와 목표 가치 입력
n, k = map(int, input().split())

# 각 동전의 가치를 저장할 리스트
coins = [int(input()) for _ in range(n)]

# 필요한 동전의 개수를 저장할 변수
count = 0

# 가치가 큰 동전부터 확인
for coin in reversed(coins):
    count += k // coin
    k %= coin

# 결과 출력
print(count)