m = []
for a in range(1000):
    k = 0
    for x in range(300):
        for y in range(300):
            if ((3*x + y > 48) or (x > y) or (4*x + y < a)) == 0:
                m.append(a)
print(max(m))