k1 = 0
m = []

for a in range (1, 100):
    k = 0
    for x in range (1, 100):
        if (x % a == 0) or ((x >= 70 and x <= 80) <= (x % 18 != 0)):
            k+= 1
    if k == 99:
        k1 += 1
        m.append(a)

print(*m)
print(k1, len(m))