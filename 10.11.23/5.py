def func(n):
    binnum = bin(n)[2:]
    b = []
    for i in binnum:
        b.append(i)
    if len(b) % 2 == 1:
        binnum += "1"
    else:
        binnum += "0"
    return int(binnum, 2)

num = func(func(func(18)))

print(num)
g = 0
j = 0

q1 = bin(876544)[2:]
k1 = int(q1[:len(q1)-3], 2)
q2 = bin(1234567899)[2:]
k2 = int(q2[:len(q2)-3], 2)

for i in range(k1 - 10, k1 + 10):
    if (func(func(func(i))) >= 876544) and (func(func(func(i))) <= 1234567899):
        g = i
        break

for n in range(k2 - 10, k2 + 10):
    if (func(func(func(n))) >= 876544) and (func(func(func(n))) <= 1234567899):
        j = n
        break

print(j - g)
# while notend:
#     print(i)
#     if (func(func(func(i))) >= int(q1[:len(q1)-3], 2)) and (func(func(func(i))) <= int(q2[:len(q2)-3], 2)):
#         k += 1
#     i += 1
#     if i == 1234567: 
#         notend = False
# print(k)