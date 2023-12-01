g = 6*343**5 + 5*49**7 - 50
print(g)
s = ''

while g != 0:
    os = str(g % 7)
    s = s + os
    
    g = g // 7
print(s.count('6'), s[::-1])
print(int(s, 7))