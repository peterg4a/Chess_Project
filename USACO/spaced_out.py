n = int(input())
Map = [0 for i in range(n)]
for i in range(n):
    line = input()
    line = line.split()
    line = [int(j) for j in line]
    Map[i] = line

#rows
a = 0
b = 0
for i in range(n):
    a1 = 0
    for j in range(1, n, 2):
        a1 += Map[i][j]
    a2 = 0
    for j in range(0, n, 2):
        a2 += Map[i][j]
    a += max(a1, a2)

    b1 = 0
    for j in range(1, n, 2):
        b1 += Map[j][i]
    b2 = 0
    for j in range(0, n, 2):
        b2 += Map[j][i]
    b += max(b1, b2)

print(max(a, b))