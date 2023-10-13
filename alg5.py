for n in range(100, 1000):
    s = str(bin(n)[2:]) 
    
    for i in range(3):
        if s.count("1") == s.count("0"):
            s += s[-1]
        elif s.count("1") > s.count("0"):
            s += "0"
        else:
            s += "1"
    r = int(s, 2) 
    if r % 4 == 0:
        print(n)
        break
    