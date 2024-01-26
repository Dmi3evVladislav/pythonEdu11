m = []
for a in range(100):
    k = 0
    for x in range(100):
        if (x&51 == 0) or ((x&41 == 0) <= (x&a == 0)):
            k+=1
    if k == 100:
        print(a)
        m.append(a)
print(max(m))