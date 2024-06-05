line = input()
line = line.split()
x = int(line[0])
y = int(line[1])
z = y - x

position = 0
total_distance = 0

for i in range(1000000000000000):
    position = 2**i * (-1)**i
    total_distance += abs(position)
    if i != 0:
        total_distance += abs(previous_position)
    
    if z >= 0:
        if position >= z:
            ans = total_distance - (position - z)
            break
    if z <= 0:
        if position <= z:
            ans = total_distance - abs(position - z)
            break

    previous_position = position
print(ans)
