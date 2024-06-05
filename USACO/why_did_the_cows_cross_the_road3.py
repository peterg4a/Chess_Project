order = []
f = open('cowqueue.in')
n = int(f.readline())
for i in range(n):
    line = f.readline()
    line = line.split()
    order.append([int(line[0]), int(line[1])])
f.close()
order.sort()
time = 0
for start, duration in order:
    if start >= time:
        time = start + duration
    else:
        time = time + duration

f = open('cowqueue.out', 'w')
f.write(str(time))
f.close()


# timeline = []
# for i in range(1000):
#     timeline.append(0)
# f = open('cowqueue.in')
# n = int(f.readline())
# for i in range(n):
#     line = f.readline()
#     line = line.split()
#     for a in range(int(line[1])):
#         timeline[int(line[0]) + a] = timeline[int(line[0]) + a] + 1
# f.close()

# time_waited = 0
# last_number = 0
# for i in range(len(timeline)):
#     if timeline[i] != 0 and timeline[i] != 1:
#         time_waited = time_waited + timeline[i] - 1
#     if timeline[i] != 0:
#         last_number = i + 1

# f = open('cowqueue.out', 'w')
# f.write(str(time_waited + last_number))
# f.close()