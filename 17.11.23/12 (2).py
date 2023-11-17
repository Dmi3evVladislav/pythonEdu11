#49

for x in range(61, 100):
    s = '1' * x
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11', 1)
    if s == '2211':
        print(s, x)
        break

