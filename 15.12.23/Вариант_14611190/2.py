for a in range(300):
    k = 0
    for x in range(300):
        for y in range(300):
            if (x + 2*y < a) or (y<x) or(y>60):
                k+= 1
    if k == 90000:
        print(a)
        break


