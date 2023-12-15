m =[]
for a in range(100):
    k = 0
    for x in range(100):
        if (x & a != 0) <= ((x & 36 == 0) <= (x & 6 != 0)):
            k+= 1
    if k == 100:
        m.append(a)

print(*m)
print(max(m))