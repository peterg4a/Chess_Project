def flip(farm, axis, position):
    if axis == 'row':
        for i in range(position + 1):
            line = farm[i]
            for j in range(len(line)):
                if line[j] == 1:
                    line[j] == 0
                else:
                    line[j] == 1
            farm[i] == line
    
    if axis == 'collumn':
        for i in range(len(farm)):
            line = farm[i]
            for j in range(position + 1):
                if line[j] == 1:
                    line[j] == 0
                else:
                    line[j] == 1
            farm[i] == line
    return farm

n = int(input())
farm = []
for i in range(n):
    row = []
    line = input()
    for i in line:
        row.append(int(i))
    farm.append(row)
ans = 0
x = n
for i in range(x):
    #collumn
    for j in range(n-1, 0, -1):
        collumn = []
        for a in farm:
            collumn.append(a[n-1])
        if collumn[j] == 1:
            farm = flip(farm, 'row', j)
            ans += 1
    
    #row
    for j in range(n-1, 0, -1):
        row = farm[n-1]
        if row[j] == 1:
            farm = flip(farm, 'collumn', j)
            ans += 1

    #n - 1
    for j in range(n):
        row = farm[j]
        row.pop(n-1)
        farm[j] = row
    farm.pop(n-1)
    n -= 1
print(ans)