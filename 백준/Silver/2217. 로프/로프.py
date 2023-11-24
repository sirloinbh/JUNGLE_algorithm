# 로프의 개수를 입력받습니다.
n = int(input())

# 각 로프가 버틸 수 있는 최대 중량을 리스트로 저장합니다.
ropes = [int(input()) for _ in range(n)]

# 로프들을 버틸 수 있는 중량을 기준으로 내림차순 정렬합니다.
# 이렇게 함으로써, 가장 무거운 중량을 들 수 있는 로프부터 접근할 수 있게 됩니다.
ropes.sort(reverse=True)

# 각 로프를 사용하여 가능한 최대 중량을 계산하기 위한 변수입니다.
max_weight = 0

# 각 로프에 대해서 반복문을 수행합니다.
for i in range(n):
    # 현재 로프와 그 전까지의 로프들을 함께 사용했을 때 들어올릴 수 있는 중량을 계산합니다.
    # i + 1은 현재 로프를 포함한 사용된 로프의 개수입니다. 
    weight = ropes[i] * (i + 1)
    
    # 지금까지 계산된 중량 중 가장 큰 값을 저장합니다.
    max_weight = max(max_weight, weight)

# 최종적으로 계산된 물체의 최대 중량을 출력합니다.
print(max_weight)