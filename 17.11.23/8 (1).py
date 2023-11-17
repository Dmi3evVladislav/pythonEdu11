from itertools import permutations

count = 0

for num in permutations('БИТКОИН'):
    count += 1

print(int(count / 2))