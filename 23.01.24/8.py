k=0
a = '012345678'
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    x = x1+x2+x3+x4+x5
                    if x1 !='0' and x.count('5')==1 and x.count('11')==0 and x.count('22')==0 and x.count('33')==0 and x.count('44')==0 and x.count('55')==0 and x.count('66')==0 and x.count('77')==0 and x.count('88')==0 and x.count('00')==0:
                        k+=1
print(k)