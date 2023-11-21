for x in range(1, 50):
    for y in range(1, 50):
        for w in range(1, 50):
            s = '0'+'1'*x + '2'*y + '3'*w + '0'
            n = s
            while not '00' in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '320', 1)
                s = s.replace('03', '3012', 1)
            if s.count('1') == 26 and s.count('2') == 54 and s.count('3') == 48:
                print(len(n))
                break
