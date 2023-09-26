m = []
for i in range(-6, 11):
    m.append(i)

def maxf(a):
    mx = m[0]
    for n in m:
        if m[n] > mx:
            mx = m[n]
    return mx

def minf(a):
    mn = m[0]
    for n in m:
        if m[n] < mn:
            mn = m[n]
    return mn

print(maxf(m))
print(minf(m))