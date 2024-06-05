f = open('buckets.in')

for a in range(10):
    line = f.readline()

    for b in range(10):
        if line[b] == 'B':
            B_y = a
            B_x = b
        if line[b] == 'L':
            L_y = a
            L_x = b
        if line[b] == 'R':
            R_y = a
            R_x = b
f.close

if B_y != L_y and B_x != L_x:
    number = abs(B_x - L_x) + abs(B_y - L_y) - 1

if B_y == L_y:
    x = [B_x, L_x]
    if L_y == R_y and R_x > min(x) and R_x > max(x):
        number = abs(b_x - L_x) + 1
    else:
        number = abs(b_x - L_x) - 1

if B_x == L_x:
    y = [B_y, L_y]
    if L_x == R_x and R_y > min(y) and R_y > max(y):
        number = abs(b_y - L_y) + 1
    else:
        number = abs(b_y - L_y) - 1



f = open('buckets.out', 'w')
f.write(str(number))
f.close