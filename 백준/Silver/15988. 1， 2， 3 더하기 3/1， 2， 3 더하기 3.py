# 테스트 케이스의 개수 T를 입력 받습니다.
T = int(input())

# 각 테스트 케이스마다의 결과를 저장할 리스트
test_cases = [int(input()) for _ in range(T)]

# 최대 값만큼 dp 배열을 만들기 위해 max() 함수 사용
max_value = max(test_cases)

# dp[i]: 숫자 i를 1, 2, 3의 합으로 나타내는 방법의 수
dp = [0] * (max_value + 1)

# 초기 조건
dp[1] = 1
if max_value >= 2:
    dp[2] = 2
if max_value >= 3:
    dp[3] = 4

# 동적 프로그래밍 진행
# i는 1, 2, 3의 합으로 표현될 수 있기 때문에 dp[i-1], dp[i-2], dp[i-3]의 합이 됩니다.
for i in range(4, max_value + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009  # 나누기 연산으로 오버플로 방지

# 결과 출력
for test_case in test_cases:
    print(dp[test_case])