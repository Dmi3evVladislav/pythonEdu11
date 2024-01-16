f = open('17_2.txt')
m = []
for q in f:
    m.append(int(q))
k, mx = 0, -1000000
for i in range(0, len(m) - 2):
    if m[i] > m[i+1] and m[i+1] < m[i + 2]:
        k += 1
        mx = max(mx, m[i+1])
print(k, mx)