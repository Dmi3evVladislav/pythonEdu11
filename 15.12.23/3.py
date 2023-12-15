def tr(a, b, c):
    return ((a+b > c) and (a + c > b) and (b + c > a))

m = []

for a in range(1, 100):
    k = 0
    for x in range(1,100):
        if not((tr(x, 11, 16) == (not(max(x, 5) > 10)))and tr(4, a, x)):
            k+= 1
    if k == 99:
        m.append(a)
print(max(m))
        