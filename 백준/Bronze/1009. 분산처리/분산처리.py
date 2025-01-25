def find_last_computer(a, b):
    last_digit = a % 10  

    if last_digit == 0:
        return 10
    elif last_digit in [1, 5, 6]:
        return last_digit
    else:
        exponent = b % 4
        if exponent == 0:
            exponent = 4
        result = last_digit
        for _ in range(exponent - 1):
            result *= last_digit
            result %= 10
        if result == 0:
            return 10
        else:
            return result

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(find_last_computer(a, b))
