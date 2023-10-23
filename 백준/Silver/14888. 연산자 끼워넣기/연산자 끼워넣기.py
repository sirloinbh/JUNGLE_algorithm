def calculate(num1, num2, operator):
    # 주어진 연산자에 따라 두 숫자를 계산하여 반환하는 함수
    if operator == 0:  # 덧셈
        return num1 + num2
    elif operator == 1:  # 뺄셈
        return num1 - num2
    elif operator == 2:  # 곱셈
        return num1 * num2
    elif operator == 3:  # 나눗셈
        if num1 < 0:
            return -(-num1 // num2)  # 음수 나누기 양수의 경우 Python 특성 상 올림 처리를 위한 코드
        return num1 // num2

def backtrack(numbers, operators, index, current_value):
    # 백트래킹을 사용하여 가능한 모든 표현식의 결과값을 구하는 함수
    if index == len(numbers):  # 모든 숫자를 사용한 경우
        return current_value, current_value  # 현재 값 반환

    min_value = float('inf')  # 최솟값 초기화
    max_value = float('-inf')  # 최댓값 초기화

    for i in range(4):  # 4개의 연산자(덧셈, 뺄셈, 곱셈, 나눗셈)에 대해
        if operators[i] > 0:  # 해당 연산자를 사용할 수 있는 경우
            next_value = calculate(current_value, numbers[index], i)  # 연산자를 사용하여 다음 값 계산
            operators[i] -= 1  # 연산자 사용 횟수 감소
            local_min, local_max = backtrack(numbers, operators, index + 1, next_value)  # 다음 숫자로 백트래킹
            min_value = min(min_value, local_min)  # 최솟값 갱신
            max_value = max(max_value, local_max)  # 최댓값 갱신
            operators[i] += 1  # 연산자 사용 횟수 복원 (백트래킹)

    return min_value, max_value  # 최솟값과 최댓값 반환

def find_min_max_expression_values():
    n = int(input())  # 숫자의 개수 입력
    numbers = list(map(int, input().split()))  # 숫자들 입력
    operator_counts = list(map(int, input().split()))  # 각 연산자의 사용 가능 횟수 입력

    min_value, max_value = backtrack(numbers, operator_counts, 1, numbers[0])  # 백트래킹 시작
    print(max_value)  # 가능한 표현식의 최댓값 출력
    print(min_value)  # 가능한 표현식의 최솟값 출력

# 주석 처리하여 실행 오류를 막습니다.
find_min_max_expression_values()