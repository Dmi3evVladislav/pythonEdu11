a = []

for x in range(4):
    for y in range(4):
        for z in range(4):
            for w in range(4):
                for g in range(4):
                    a.append(str(x)+str(y)+str(z)+str(w)+str(g))
                    # a.append(x,y,z,w,g)

k = 0
for (i) in a:
    k += 1
    if i[0] == "3":
        print(k, i)