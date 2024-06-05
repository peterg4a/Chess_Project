n = int(input())
cordinates = {}
for i in range(1001):
    for j in range(1001):
        cordinates[i,j] = 0
x = [0, 0, -1, 1]
y = [1, -1, 0, 0]
comfort = {}
output = []

for i in range(n):
    line = input()
    line = line.split()
    cordinate = [int(line[0]), int(line[1])]
    cordinates[cordinate[0], cordinate[1]] = 1
    comfort[cordinate[0], cordinate[1]] = 0

    for j in range(4):
        adjacent = [cordinate[0] + x[j], cordinate[1] + y[j]]
        if adjacent[0] >= 0 and adjacent[1] >= 0:
            if cordinates[adjacent[0], adjacent[1]] == 1:
                comfort[adjacent[0], adjacent[1]] += 1
                comfort[cordinate[0], cordinate[1]] += 1

    num = 0
    current_comfort = comfort.values()
    for a in current_comfort:
        if a == 3:
            num += 1
    print(num)