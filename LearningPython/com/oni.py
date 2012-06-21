import math, random
def ranarr(n):
    x = {}
    for i in range(n):
        x[i] = int( math.ceil(n * random.random()))
    return x
print ranarr(10)
a = ranarr(10)
b = ranarr(10)
c = 6
adict = {}
for i in a.values():
    for j in b.values():
        if i+j == c:
            print i, j
print "_-------_"
for i in a.values():
    if c-i in b.values():
        print i, c-i
print "_-------_"

for i in a.values():
    adict[c-i] = c-i    
for j in b.values():
    if j in adict.keys():
        print c-j, j
