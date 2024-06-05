f = open('billboard.in')
billboard1_input = f.readline()
billboard1_input = billboard1_input.split()
billboard1 = [int(i) for i in billboard1_input]
billboard1_area = (billboard1[3] - billboard1[1]) * (billboard1[2] - billboard1[0])

billboard2_input = f.readline()
billboard2_input = billboard2_input.split()
billboard2 = [int(i) for i in billboard2_input]
billboard2_area = (billboard2[3] - billboard2[1]) * (billboard2[2] - billboard2[0])

area = billboard1_area + billboard2_area

truck_input = f.readline()
truck_input = truck_input.split()
truck = [int(i) for i in truck_input]

f.close()

if truck[0] >= billboard1[2] or truck[2] <= billboard1[0]:
    overlap1 = 0
else:
    if truck[1] >= billboard1[3] or truck[3] <= billboard1[1]:
        overlap1 = 0
    else:
        x = [truck[0], truck[2], billboard1[0], billboard1[2]]
        x.sort()
        overlap_x = x[2] - x[1]

        y = [truck[1], truck[3], billboard1[1], billboard1[3]]
        y.sort()
        overlap_y = y[2] - y[1]

        overlap1 = overlap_x * overlap_y

if truck[0] >= billboard2[2] or truck[2] <= billboard2[0]:
    overlap2 = 0
else:
    if truck[1] >= billboard2[3] or truck[3] <= billboard2[1]:
        overlap2 = 0
    else:
        x = [truck[0], truck[2], billboard2[0], billboard2[2]]
        x.sort()
        overlap_x = x[2] - x[1]

        y = [truck[1], truck[3], billboard2[1], billboard2[3]]
        y.sort()
        overlap_y = y[2] - y[1]

        overlap2 = overlap_x * overlap_y

ans = area - overlap1 - overlap2
f = open('billboard.out', 'w')
f.write(str(ans))
f.close()