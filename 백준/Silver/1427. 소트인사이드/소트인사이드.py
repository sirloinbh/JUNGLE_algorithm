N = int(input())
digits_array = [int(digit) for digit in str(N)]
digits_array.sort()
digits_array.reverse()
N = [str(digit) for digit in digits_array]
print(''.join(N))
