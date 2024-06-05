possible_i = []
f = open('factory.in')
n = int(f.readline())
for i in range(n):
    possible_i.append(i+1)
for i in range(n - 1):
    line = f.readline()
    line = line.split()
    if line[0] in possible_i:
        possible_i.remove(line[0])
f.close()

f = open('factory.out','w')
if len(possible_i) == 1:
    f.write(str(possible_i[0]))
else:
    f.write('-1')