for N in range(1000, 0, -1):
    binN = str(bin(N)[2:])
    if N % 3 == 0:
        binN += binN[-3:]
    else:
        binN += str(bin(3* (N % 3))[2:])
    print(int(binN, 2))
    if (int(binN, 2) < 100):
        print("------")
        print(N)
        break
        
        

# str = "последние три"
# str+=str[-3:]
# print(str)

# N = 9
# binN = str(bin(N)[2:])
# print("начальное", binN)
# if N % 3 == 0:
#     binN += binN[-3:]
#     print("1 усл", binN)
# else:
#     print(str(bin(3* (N % 3))[2:]))
#     binN += str(bin(3* (N % 3))[2:])
#     print("2 усл", binN)
# print(int(binN, 2))