def fun(N):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += R[:2:1]
    if N % 2 != 0:
        R = "1" + R + "0"
    return int(R, 2)


for i in range(0, 1000):
    if fun(i) < 100:
         print(i)
    