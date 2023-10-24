n = 345
w =''
while n>0:
    w += str(n%3)
    n = n//3
print(w[::-1])