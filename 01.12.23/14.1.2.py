g = 2*216**6 + 3*36**9 -432
print(g)
s = ''

while g != 0:
    os = str(g % 6)
    s = s + os
    
    g = g // 6
print(s.count('5'), s[::-1])