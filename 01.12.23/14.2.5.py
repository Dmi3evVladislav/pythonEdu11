n = 5**55 + 5**555 * 555 - 5
m = [0] * 5
while n != 0:
    os = n % 5
    m[os] = m[os] + 1
    n = n // 5
print(*m)