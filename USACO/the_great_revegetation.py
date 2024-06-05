def find_loop(land):
    global passed
    global loop
    loop[land] = 1
    passed[land] = True
    for i in connections[land]:
        #if it does not connects back
        if loop[i] == 0:
            find_loop(i)
        
line = input().split()
n, m = int(line[0]), int(line[1])
connections = ['null']
passed = ['null']
for i in range(n):
    connections.append([])
    passed.append(False)

for i in range(m):
    line = input().split()
    connections[int(line[1])].append(int(line[2]))
    connections[int(line[2])].append(int(line[1]))

loops = 0
for i in range(n):
    if passed[i] == False:
        loops += 1
        loop = ['null']+[0 for i in range(n)]
        find_loop(i)

ans = '1'
for i in range(loops):
    ans += '0'
print(ans)
