import math

def calc(x,f):
    num = 0
    for i in area:
        if x < i:
            num += math.floor(i / x)
    if num >= f:
        return True
    else:
        return False

cases = int(input())
for i in range(cases):
    line = input()
    line = line.split()
    n,f = [int(j) for j in line]
    f += 1
    line = input()
    line = line.split()
    radii = [int(j) for j in line]
    area = [math.pi * (j**2) for j in radii]

    l,r = 0,max(area)
    for j in range(100):
        mid = (l+r)/2
        if calc(mid, f):
            l = mid
        else:
            r = mid
    
    print(round(mid, 4))
    