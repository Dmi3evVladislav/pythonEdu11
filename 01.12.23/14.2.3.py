g = 2**5*3**25
s = ''

while g != 0:
    os = str(g % 3)
    s = s + os
    
    g = g // 3
print(s.count('1'), s.count('2'))