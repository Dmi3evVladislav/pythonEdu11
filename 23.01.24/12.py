m = 0
for i in range(4, 10000):
    str = "3" + "5"*i
    while "333" in str or "555" in str:
        if "555" in str: 
            str = str.replace("555", "3", 1)
        else:
            str = str.replace("333", "5", 1)
    sm = str.count('3')*3 + str.count('5')*5
    m = max(m, sm)
    print(m)
