# 주어진 수식을 입력받는다.
expression = input().split('-')

# 최종 결과를 저장할 변수
result = 0

# 첫 번째 '-' 이전의 수식 계산
# '-'로 나뉜 첫 번째 부분만 '+' 연산이 되므로 결과에 더한다.
for num in expression[0].split('+'):
    result += int(num)  # '+' 연산을 수행하여 결과에 더함

# 첫 번째 '-' 이후의 수식 계산
# 이 부분에서는 모든 값을 빼야 하므로 '-' 연산을 수행한다.
for sub_exp in expression[1:]:
    # 각 '-'로 나뉜 부분에 대하여 '+' 연산을 수행
    for num in sub_exp.split('+'):
        result -= int(num)  # 해당 부분의 합을 결과에서 뺀다.

# 최종 결과 출력
print(result)