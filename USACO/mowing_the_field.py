n = int(input())
motions = []
for i in range(n):
    line = input()
    line = line.split()
    line[1] = int(line[1])
    motions.append(line)


x = -1
time = 0
coordinate = [0, 0]
mowed_coordinates = [coordinate[:]]

for motion in motions:
    for i in range(motion[1]):
        if motion[0] == 'N':
            coordinate[1] += 1
        if motion[0] == 'S':
            coordinate[1] -= 1
        if motion[0] == 'E':
            coordinate[0] += 1
        if motion[0] == 'W':
            coordinate[0] -= 1
        print(mowed_coordinates)
        print(x, coordinate)
        if coordinate in mowed_coordinates:
            if mowed_coordinates.index(coordinate) > x:
                x = mowed_coordinates.index(coordinate)

        mowed_coordinates.insert(0, coordinate[:])
        
print(x)
