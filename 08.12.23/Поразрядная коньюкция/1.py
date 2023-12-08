for a in range(1000):
    k = 0
    for x in range(1000):
        if (x & 51 == 0) or ((x & 41 == 0) <= (x & a == 0)):
            k += 1
    if k == 1000:
        print(a)