for n in range(0, 1000):
    s = str(bin(n)[2:]) 
    sum = s.count('1')
    s += str(sum % 2)
    sum = s.count('1')
    s += str(sum % 2)
    if (int(s, 2) > 85):
        print(n)
        break
