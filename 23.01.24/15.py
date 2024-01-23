for a in range(1, 1000):
    for x in range(1, 1000):
        if ((x&a==0) or not (x&37==0) or (not (x&12==0)))==0:
            break
    else:
        print(a)