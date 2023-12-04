g = 4**16 + 2**36 - 8
s = ''

while g != 0:
    os = str(g % 2)
    s = s+os
    
    g = g // 2
print(s.count('1'), s[::-1])