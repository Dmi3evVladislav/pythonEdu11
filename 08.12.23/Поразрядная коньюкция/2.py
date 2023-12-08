for a in range(100):
    k = 0
    for x in range(100):
        if ((x&28!=0)or(x&45!=0))<=((x&48 == 0)<=(x&a!=0)):
            k += 1
    if k == 100:
        print(a)
        break