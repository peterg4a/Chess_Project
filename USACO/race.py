def solve(dist, minspedd):

    l = 0
    r = 0
    time = 0
    cur = 1
    while True:
        l += cur
        time +=1
        if l+r >=dist :
            return time
        if cur >= minspedd:
            r += cur
            time +=1
            if l+r >=dist:
                return time
        cur += 1

f = open('race.in')

k, n = map(int, f.readline().split())
#k, n = map(int, input().split())


num = []
for i in range(n):
    a = int(f.readline())
    num.append(a)
f.close()
f = open('race.out', 'w')

for i in range(n):
    f.write(str(solve(k, num[i]))+'\n')
    #print(solve(k, num[i]))    
f.close()