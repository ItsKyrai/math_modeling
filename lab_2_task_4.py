a = [0, 1]
n = int(input())
for i in range(n-2):
    b = a[-1] + a[-2]
    a.append(b)
print(a)