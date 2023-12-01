n = (66+6**2019)*6**2019+66+6**6
m = [0]*10000
i, s = 0, 0
while n != 0:
    os = n % 5
    m[i] = m[i] + os
    s = s + os
    n = n // 5
    i +=1
print(sum(m), s)
