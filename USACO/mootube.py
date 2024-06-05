def calc(k,v,previous):
    ans = 0
    for i in Map[v-1]:
        if i[0] != previous:
            if i[1] >= k:
                ans += 1
                ans += calc(k, i[0], v)
    return ans

f = open('mootube.in')
line = f.readline()
line = line.split()
line = [int(i) for i in line]
n, q = line

Map = []
for i in range(n):
    Map.append([])

for i in range(n-1):
    line = f.readline()
    line = line.split()
    x = [int(i) for i in line]
    Map[x[0]-1].append([x[1], x[2]])
    Map[x[1]-1].append([x[0], x[2]])

questions = []
for i in range(q):
    line = f.readline()
    line = line.split()
    line = [int(i) for i in line]
    questions.append(line)
f.close()
f = open('mootube.out', 'w')
for i in questions:
    f.write(str(calc(i[0],i[1],0)) + '\n')
f.close()