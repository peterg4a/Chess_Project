n = int(input())
line = input()
line = line.split()
cows = [int(i) for i in line]
line = input()
line = line.split()
rooms = [int(i) for i in line]

difference = []
for i in range(n):
    difference.append(rooms[i] - cows[i])
# print(difference)
groups = []
group = []
for i in range(n):
    if i == 0 and difference[i] != 0:
        group.append(difference[i])
        previous = difference[i]
    elif i== 0 and difference[i] == 0:
        previous = difference[i+1]
    else:
        if difference[i] > 0 and previous > 0:
            group.append(difference[i])
        elif difference[i] < 0 and previous < 0:
            group.append(difference[i])
        elif difference[i] == 0:
            groups.append(group)
            group = []
            previous = difference[i + 1]
        else:
            groups.append(group)
            group = [difference[i]]
            previous = difference[i]
groups.append(group)
# print(groups)
for group in groups:
    for i in range(len(group)):
        if group[i] < 0:
            group[i] *= -1
# print(groups)
ans = 0
for group in groups:
    previous = 0
    for i in group:
        if i > previous:
            ans += i - previous
        previous = i
print(ans)