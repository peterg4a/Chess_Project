def dfs(u, indicator):
    if group[u]:
        return
    visit[u] = 1
    group[u] = indicator
    for child in paths[u]:
        if (breed[child] == breed[u] ):
            dfs(child, indicator)

line = input()
line = line.split()
n, m = int(line[0]), int(line[1])
breed = '0' + input()
paths = [[] for i in range(n+1)]
for i in range(n-1):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    paths[line[0]].append(line[1])
    paths[line[1]].append(line[0])
answer = ''

indicator = 1

group = [0 for i in range(n+1) ]
visit= [0 for i in range(n+1) ]

for i in range(1, n+1):
    if visit[i] == 0:
        dfs(i, indicator)
        indicator += 1

for i in range(m):
    line = input()
    line = line.split()
    s, e, b = int(line[0]), int(line[1]), line[2]

    if (breed[s] == b or group[s] != group[e]):
        print(1)
    else:
        print(0)