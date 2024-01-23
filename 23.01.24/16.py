f = [0] * 2100
for n in range(2100):
    if n <= 3:
        f[n] = 1
    else:
        f[n] = (n + 3) * f[n - 2]
print(f[2028] / f[2024])