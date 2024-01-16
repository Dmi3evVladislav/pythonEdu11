f = open('17_2.txt')
m = []
for q in f:
    m.append(int(q))
k, mx = 0, -10000000
for i in range(len(m)-1):
    if (m[i] % 7 == 0 and m[i+1] % 17 !=0) or (m[i+1] % 7 == 0 and m[i] % 17 !=0):
        k+=1
        s = m[i] + m[i+1]
        mx = max(mx, s)
print(k, mx)