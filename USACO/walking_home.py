# Coordinates contain collumn, row, previous direction
def calc(coordinate):
    x, y, direction, count = coordinate
    possibilities = []
    if x < n-1:
        if barn[x+1][y] != 'H':
            if direction != 'R':
                if count+1 <= k:
                    possibilities.append([x+1, y, 'R', count+1])
            else:
                possibilities.append([x+1, y, 'R', count])
    if y < n-1:
        if barn[x][y+1] != 'H':
            if direction != 'D':
                if count+1 <= k:
                    possibilities.append([x, y+1, 'D', count+1])
            else:
                possibilities.append([x, y+1, 'D', count])
    return possibilities

z = int(input())
for i in range(z):
    line = input()
    line = line.split()
    n, k, = int(line[0]), int(line[1])
    barn = []
    for i in range(n):
        line = input()
        row = []
        for j in range(len(line)):
            row.append(line[j])
        barn.append(row)
    # print(barn)

    cords = [[0, 0, 'none', -1]]
    temp_cords = []
    for i in range((n-1)*2):
        for cord in cords:
            a = calc(cord)
            for j in a:
                temp_cords.append(j)
        cords = []
        for j in temp_cords:
            cords.append(j)
        temp_cords = []
    print(len(cords))
