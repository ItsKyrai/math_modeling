a = int(input())
if a % 4 == 0 or a % 400 == 0:
    if a % 100 == 0:
        print('Год не високосный')
    else:
        print('Год високосный')
else:
    print('Год не високосный')