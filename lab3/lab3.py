print("Введіть числа через пробіл: ")
numlist = list(map(int, input().split()))
for a in numlist:
    for b in numlist:
        if a + b == 10:
            print(a , "+" ,b)