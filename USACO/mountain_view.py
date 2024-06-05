n = int(input())
mountains = []
for i in range(n):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    mountains.append(line)

for i in mountains:
    x = i[0]
    y = i[1]
    i[0] = x-y
    i[1] = x+y
mountains.sort()
print(mountains)
visibility = []
for i in range(n):
    visibility.append(True)

for i in range(n):
    if i == 0:
        dominant_mountain = mountains[0]
        dominant_position = 0
    else:
        mountain = mountains[i]
        if mountain[0] == dominant_mountain[0] and mountain[1] > dominant_mountain[1]:
            visibility[dominant_position] = False
            dominant_mountain = mountain
            dominant_position = i
        elif mountain[0] > dominant_mountain[0] and mountain[1] > dominant_mountain[1]:
            dominant_mountain = mountain
            dominant_position = i
        else:
            visibility[i] = False
    print(dominant_position)
    print(visibility)
ans = 0
for i in visibility:
    if i:
        ans += 1
print(ans)