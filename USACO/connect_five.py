def in_a_row(List, status):
    max_connect = 0
    connect = 0
    for i in List:
        if i == status:
            connect += 1
        else:
            connect = 0
        if connect > max_connect:
            max_connect = connect
    if max_connect >= 5:
        return True
    return False

def calc(x, y, status):
    #horizontal
    row = Map[x-1]
    collumn = []
    for i in range(15):
        collumn.append(Map[i][y-1])
    
    left = []
    if x > y:
        xx = x-y
        yy = 1
    else:
        yy = y-x
        xx = 1
    print(xx, yy)
    while xx <= 15 and yy <= 15:
        left.append(Map[xx-1][yy-1])
        xx += 1
        yy += 1
    print(left)

    right = []
    if x + y > 15:
        xx = x - y
        yy = 15
    else:
        xx = 1
        yy = x + y
    
    while xx <= 15 and yy >= 1:
        right.append(Map[xx-1][yy-1])
        xx += 1
        yy -= 1

    List = [row, collumn, left, right]
    for i in List:
        if in_a_row(i, status):
            return True
    return False

n = int(input())
Map = []
for i in range(15):
    row = []
    for j in range(15):
        row.append('0')
    Map.append(row)

moves = []
for i in range(n):
    line = input()
    line = line.split()
    x, y = [int(i) for i in line]
    moves.append([x,y])

for i in range(n):
    if i%2 == 0:
        status = 'A'
    else:
        status = 'B'

    x, y = moves[i]
    Map[x-1][y-1] = status

    if calc(x, y, status):
        print(status, i+1)
        break
    if i == n-1:
        print('Tie')
for i in Map:
    print(i)