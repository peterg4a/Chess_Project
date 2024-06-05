line = input()
line = line.split()
line = [int(i) for i in line]
L, n, rf, rb = line
r = rf - rb
stops = []
for i in range(n):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    stops.append(line)

total_pleasure = 0

stops.sort(key = lambda x : -x[1])

position = -1
previous_position = 0
for i in range(len(stops)):
    a = stops[i]
    if a[0] > position:
        position = a[0]
        pleasure = (position - previous_position) * r * a[1]
        print(position, previous_position, r, a[1])
        total_pleasure += pleasure
        previous_position = position
print(total_pleasure)