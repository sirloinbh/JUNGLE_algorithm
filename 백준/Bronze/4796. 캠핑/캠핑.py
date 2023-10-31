case_num = 0
while True:
    case_num += 1
    L, P, V = map(int, input().split())

    # 종료 조건: L, P, V가 모두 0일 때
    if L == 0 and P == 0 and V == 0:
        break

    # 캠핑을 할 수 있는 최대 일 수 계산
    result = (V // P) * L + min(V % P, L)
    print(f"Case {case_num}: {result}")