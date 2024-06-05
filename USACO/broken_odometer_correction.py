def check(mid):
    tot_t = 0
    for i in range(n):
        si = S[i]
        di = D[i]
        
        v = mid + si
        if v < 0:
            return true
        ti = di / v
        tot_t += ti
    return tot_t > t

line = input()
line = line.split()
n, t = int(line[0]), int(line[1])
S = []
D = []
for i in range(n):
    line = input()
    line = line.split()
    s, d = int(line[0]), int(line[1])
    S.append(s)
    D.append(d)

l = -1e9
r = 1e9

mid = (l+r )/ 2

while r - l > 1e-6 :
    if check(mid):
        l = mid
    else:
        r = mid
    mid = (l+r )/ 2
    
print(l)