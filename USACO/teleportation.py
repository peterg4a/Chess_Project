journey = []
teleporter = []
f = open('teleport.in')
line = f.readline()
f.close()
line = line.split()
journey.append(int(line[0]))
journey.append(int(line[1]))
teleporter.append(int(line[2]))
teleporter.append(int(line[3]))
journey.sort()
teleporter.sort()

if abs(journey[0] - teleporter[0]) + abs(journey[1] - teleporter[1]) < journey[1] - journey[0]:
    distance = abs(journey[0] - teleporter[0]) + abs(journey[1] - teleporter[1])
else:
    distance = journey[1] - journey[0]

f = open('teleport.out', 'w')
f.write(str(distance))
f.close()