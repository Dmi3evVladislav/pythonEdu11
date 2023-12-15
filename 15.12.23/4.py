def tr(a, b, c):
    return ((a+b > c) and (a + c > b) and (b + c > a))

m = []

for a in range(1, 100):
    k = 0
    for x in range(1,100):
        if ((tr(x,10,20) <= (not(max(x, 8) > 24))) == (not(tr(3, a, x)))):
            k+= 1
    if k == 99:
        m.append(a)
print(max(m))