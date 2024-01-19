f = open('17_10100.txt')
m = []
for q in f:
    m.append(int(q))

mxp = 0    
for i in range(len(m)):
    if m[i] % 100 == 13:
        if m[i] > mxp:
            mxp = m[i]
k  = mx = 0
for i in range(len(m)-2):
    s = (100<=m[i]<=999)+(100<=m[i+1]<=999)+(100<=m[i+2]<=999) # интересный подход
    su = m[i]+m[i+1]+m[i+2]
    if s==2 and su <= mxp:
        k += 1
        mx=max(su, mx)
print(k, mx)