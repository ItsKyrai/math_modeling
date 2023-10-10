a = []
b = int(input())
q = int(input())
n = int(input())
for i in range(n):
    b1 = b * q
    a.append(b1)
    b = b1
print(a)