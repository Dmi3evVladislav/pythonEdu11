
for a in range(1, 100):
    k = 0
    for x in range(1, 100):
        if (x % a == 0) <= ((x % 21 == 0) + (x%35 == 0)):
            k+= 1
    if k == 99:
        print(a)
        break
