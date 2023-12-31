menu = [int(input()) for _ in range(5)]
burger = min(menu[0:3])
beverage = min(menu[3:5])
print(burger+beverage-50)