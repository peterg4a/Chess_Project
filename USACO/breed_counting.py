#Remember to use sum() - sum()
line = input()
line = line.split()
line = [int(i) for i in line]
n, q = line

cows = []
for i in range(3):
    l = []
    for i in range(100001):
        l.append(0)
    cows.append(l)

for i in range(n):
    x = int(input())
    cows[x-1][i+1] = 1

for i in range(3):
    for j in range(1, 100001):
        cows[i][j] += cows[i][j-1]

queries = []
for i in range(q):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    queries.append(line)

for i in range(q):
    query = queries[i]
    line = ''
    for j in range(3):
        x = cows[j][query[1]] - cows[j][query[0]- 1]
        line += str(x)
        if j != 2:
            line += ' '
    if i != q:
        line += '\n'
    print(line)