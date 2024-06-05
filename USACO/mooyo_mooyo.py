line = input()
line = line.split()
n, k = int(line[0]), int(line[1])
Map = [['null' for i in range(n)] for i in range(10)]
for i in range(n-1, -1, -1):
    line = input()
    line = [int(j) for j in line]
    for j in range(10):
        Map[j][i] = line[j]
print(Map)
