n = (77+7**77)*7**77+77+7**7
m = [0] * 7
while n != 0:
    os = n % 7
    m[os] = m[os] + 1
    n = n // 7
print(*m)