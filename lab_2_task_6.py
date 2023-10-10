for i in range(1, 10):
    a = []
    for c in range(1, 10):
        a.append(i * c)
    print(*a, sep="  ")