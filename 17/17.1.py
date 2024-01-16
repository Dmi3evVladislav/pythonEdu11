f = open('17.1.txt')
m = []
for q in f:
    m.append(int(q))

# t = [0, 1, 2]
# for j in range(len(t)):
#     print(t[j])
    
k, mx = 0, -100000

for i in range(len(m) - 1):
    if m[i] % 3 == 0 or m[i+1] % 3 == 0:
        k += 1
        s = m[i] + m[i+1]
        # mx = max(mx, s)
        if s > mx:
            mx = s

print(k, mx)