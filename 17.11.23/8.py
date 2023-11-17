from itertools import product

count = 0

for num in product('0234567', repeat=5):
    if num[0] == '0':
        continue
    if len(set(num)) != 5:
        continue
    for i in range(4):
        if int(num[i])%2 == int(num[i + 1])%2:
            break
    else:
        count += 1
print(count)