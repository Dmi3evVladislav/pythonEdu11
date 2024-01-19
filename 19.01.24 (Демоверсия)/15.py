for a in range(1000):
    k = 0
    for x in range(500):
        for y in range(500):
            if (x+2*y<a)or(y>x)or(x>60):
                k+=1
    if k == 500*500:
        print(a)
        break