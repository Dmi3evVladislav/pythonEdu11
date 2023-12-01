n = 4**16 + 2**34 - 8

k = 0

while n != 0:
    os = n % 2
    if os == 1:
        k += 1
    n = n // 2
print(k)

g = 4**16 + 2**34 - 8
s = ''

while g != 0:
    os = str(g % 2)
    s = s+os
    
    g = g // 2
print(s.count('1'), s[::-1])