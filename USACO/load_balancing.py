line = input()
line = line.split()
n = int(line[0])
B = int(line[1])
cows = []
for i in range(n):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    cows.append(line)

#Find a
best_a = 0
best_a_max = 1000000000
best_a_side = 'none'
for i in range(2, B+1, 2):
    left = 0
    right = 0
    for j in cows:
        if j[0] < i:
            left += 1
        else:
            right += 1
    #Define best_a
    if max(left, right) < best_a_max:
        best_a = i
        best_a_max = max(left, right)
        if max(left, right) == left:
            best_a_side = 'left'
        if max(left, right) == right:
            best_a_side = 'right'
    if i != 2:
        if max(left, right) > previous_max:
            break
    previous_max = max(left, right)
print(best_a, best_a_max, best_a_side)

#Find smallest possible largest quadrant(M)
best_M = 1000000000000
for i in range(2, B+1, 2):
    up = 0
    down = 0
    for j in cows:
        # left
        if best_a_side == 'left':
            if j[0] < best_a:
                if j[1] > i:
                    up += 1
                else:
                    down += 1
        # right
        else:
            if j[0] > best_a:
                if j[1] > i:
                    up += 1
                else:
                    down += 1
    if max(up, down) < best_M:
        best_M = max(up, down)
    if i != 2:
        if max(up, down) > previous_max:
            break
    previous_max = max(up, down)
print(best_M)