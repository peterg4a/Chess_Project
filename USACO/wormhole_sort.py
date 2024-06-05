line = input().split()
n,m = int(line[0]), int(line[1])

line = input().split()
cows = [int(i) for i in line]

all_wormholes = []
for i in range(m):
    line = input().split()
    line = [int(i) for i in line]
    all_wormholes.append(line)
all_wormholes.sort(key=lambda x: x[2])
print(all_wormholes)

out_of_order = []
for i in range(n):
    if cows[i] != i+1:
        out_of_order.append(i+1)
print(out_of_order)

wormholes = []
connected = [False for i in range(n)]
for i in range(m-1, -1, -1):
    print(wormholes)
    print(connected)
    con = True
    for j in out_of_order:
        if connected[j-1] == False:
            con = False
    if con == True:
        if len(wormholes) != 0:
            print(wormholes[-1][2])
        else:
            print(-1)
    else:
        x = all_wormholes[i]
        wormholes.append(x)
        connected[x[0]-1] = True
        connected[x[1]-1] = True