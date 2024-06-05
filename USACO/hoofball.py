lonely_cows = []
f = open('hoofball.in')
n = int(f.readline())
cows = f.readline()
f.close()
cows = cows.split()
cows = [int(i) for i in cows ]
cows.sort()
balls = 1
directions = []
for i in range(n):
    directions.append(0)
direction_change = 0
for i in range(n):
    if i == 0:
        directions[i] = 1
    elif i == n - 1:
        directions[i] = -1
    elif i != 0 and i != n - 1:
        l = abs(cows[i] - cows[i - 1])
        r = abs(cows[i] - cows[i + 1])

        if l <= r:
            directions[i] = -1
        else:
            directions[i] = 1
    
    if i != 0:
        if directions[i] != directions[i - 1]:
            direction_change = direction_change + 1
    
    if direction_change == 1:
        balls = balls + 1
        direction_change = 0

f = open('hoofball.out', 'w')
f.write(str(balls))
f.close()