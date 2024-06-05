f = open('crossroad.in')
n = int(f.readline())
positions = {}
crosses = 0
for i in range(n):
    line = f.readline()
    line = line.split()

    cow_number = int(line[0])
    cow_position = int(line[1])

    if cow_number not in positions:
        positions[cow_number] = cow_position
    
    else:
        if cow_position != positions[cow_number]:
            crosses = crosses + 1
            positions[cow_number] = cow_position
        else:
            positions[cow_number] = cow_position
f.close()

f = open('crossroad.out', 'w')
f.write(str(crosses))
f.close()