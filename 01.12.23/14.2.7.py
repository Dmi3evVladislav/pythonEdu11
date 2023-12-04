n = int(input())
s =''

while n != 0:
    os = str(n % 6)
    s = s + os
    if n%6 == 0:
        s = s + '0'
    
    n = n // 6
print(int(s))