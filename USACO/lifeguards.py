f = open('lifeguards.in')
n = int(f.readline())
cows = []
day = []
for i in range(1001):
    day.append(0)
for i in range(n):
    line = f.readline()
    line = line.split()
    cow = [int(line[0]), int(line[1])]
    cows.append(cow)
    a = cow[0]
    b = cow[1]
    for j in range(b-a):
        day[a + j + 1] += 1
f.close()
longest_time = 0
for i in cows:
    time = 0
    a = i[0]
    b = i[1]
    for j in range(b-a):
        day[a + j + 1] -= 1
    for j in day:
        if j > 0:
            time += 1
    if time > longest_time:
        longest_time = time
    for j in range(b-a):
        day[a + j + 1] += 1
f = open('lifeguards.out', 'w')
f.write(str(longest_time))
f.close()