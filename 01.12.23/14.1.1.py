g = 125**4 + 25**8 - 30
print(g)
s = ''

while g != 0:
    os = str(g % 5)
    s = s + os
    
    g = g // 5
print(s.count('4'), s[::-1])