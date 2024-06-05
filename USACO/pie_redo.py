def calc(vol):
    num = 0
    for i in pies:
        x = i//vol
        num += x
    print(i, vol)
    print(num)
    return num

z = int(input())
for i in range(z):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    n, f = line
    f += 1
    line = input()
    line = line.split()
    pies = [(int(i)**2)*3.1415926 for i in line]
    print(pies)
    
    l = 0
    r = 1000000000
    for i in range(50):
        m = (l+r)/2
        if calc(m) >= f:
            l = m
        else:
            r = m
    print(l)