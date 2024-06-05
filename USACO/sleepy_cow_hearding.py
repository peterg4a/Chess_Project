f = open('herding.in')
line = f.readline()
line = line.split()
positions = [int(i) for i in line]
f.close

if positions[0] + 1 == positions[1] and positions[1]+ 1 == positions[2]:
    minimum = 0
    maximum = 0

elif positions[1] - positions[0] == 2 or positions[2] - positions[1] == 2:
    minimum = 1
    a = positions[1] - positions[0]
    b = positions[2] - positions[1]
    if a >= b:
        maximum = a
    if b > a:
        maximum = b
    
    maximum = maximum - 1

else:
    minimum = 2
    a = positions[1] - positions[0]
    b = positions[2] - positions[1]
    if a >= b:
        maximum = a
    if b > a:
        maximum = b
    
    maximum = maximum - 1


f = open('herding.out', 'w')
f.write(str(minimum)+'\n')
f.write(str(maximum))
f.close()