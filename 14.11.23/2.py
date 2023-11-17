print("x z y w f1 f2")

def f1(x, y, z, w):
    if ((x <= y) == (w or not(z))) == 1:
        return 1
    else:
        return 0
    
def f2(x, y, z, w):
    if ((x <= y) and (not(w) == z)) == 1:
        return 1
    else:
        return 0


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, z, y, w, f1(x, y, z, w), f2(x, y, z, w))