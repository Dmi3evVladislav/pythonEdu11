file = open("17.txt")
a = []
for i in file:
    a.append(int(i))
a.sort()
for n in range(0, len(a)):
    for j in range(0, len(a)):

print(a)