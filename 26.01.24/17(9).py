f = open('17.txt')
m = []
k = 0
for q in f:
    m.append(int(q))
v =0
for i in range(len(m) - 2): 
    g = sorted((m[i], m[i+1], m[i+2]))
    if (g[2]**2 == (g[1]**2 + g[0]**2)):
        k+=1
        v = max(v, sum(11))
print(k, v)