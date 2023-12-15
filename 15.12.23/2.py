m = []
for a in range (1, 100):
    k = 0
    for x in range(1, 100):
        if (x % a == 0) or ((x >= 50 and x <= 70) <= (x % 16 != 0)):
            k+= 1
    if k == 99:
        m.append(a)
print(max(m))