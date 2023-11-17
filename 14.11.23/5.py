def func(n):
    bin_n = bin(n)[2:]
    summ = 0
    for i in bin_n:
        summ += int(i)
    bin_n += str(summ % 2)
    # print("f1", bin_n)
    summ2 = 0
    for i in bin_n:
        summ2 += int(i)
    bin_n += str(summ2 % 2)
    # print("f2", bin_n)
    return bin_n

func(2)

for r in range(0, 1000):
    if int(func(r), 2)>=123:
        print(r, func(r), int(func(r), 2))
        break
