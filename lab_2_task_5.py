a = int(input())
b = int(input())
if b ==0:
    print('На ноль делить нельзя')
elif a % b == 0:
    print(f'True, {int(a / b)}')
else:
    print(f'False, {a % b}, {a // b}')