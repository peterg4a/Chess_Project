import math
line = input()
line = line.split()
n, t = int(line[0]), int(line[1])
d = []
sc = []
for i in range(n):
    line = input()
    line = line.split()
    line = [int(j) for j in line]
    d.append(line[0])
    sc.append(line[1])

l = -10**6
r = 10**6
for i in range(20):
    mid = (l+r)/2
    print('X',mid)
    total_sub_time = 0
    go = True
    for j in range(n):
        v = (sc[j]+mid)
        if v > 0:
            sub_time = d[j]/v
            total_sub_time += sub_time
        else:
            go = False
            break
    if go:
        print(total_sub_time)
        if total_sub_time > t:
            r = mid
        elif total_sub_time < t:
            l = mid
    else:
        r = mid
        print('v is less than 0')
print(round(mid, 6))
