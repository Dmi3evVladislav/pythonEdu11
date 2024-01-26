n = 49**7 + 7**20 - 28
s = ''
while n != 0:
    s += str(n % 7)
    n = n // 7
print(s.count('6'))