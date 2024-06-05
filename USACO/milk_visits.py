def pathfind(s, e, b, satisfied, past):
    global answer
    if breed[s] == b:
        satisfied = 1
    if s == e:
        answer += str(satisfied)
        return
    for i in paths[s]:
        if i != past:
            pathfind(i, e, b, satisfied, s)


line = input()
line = line.split()
n, m = int(line[0]), int(line[1])
breed = '0' + input()
paths = [[] for i in range(n+1)]
for i in range(n-1):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    paths[line[0]].append(line[1])
    paths[line[1]].append(line[0])
answer = ''
for i in range(m):
    line = input()
    line = line.split()
    s, e, b = int(line[0]), int(line[1]), line[2]

    pathfind(s, e, b, 0, 'null')
#            start, end, breed, satisfied?, previousNode
print(answer)

# def pathfind(s, e, b, satisfied, past):
#     global answer
#     if breed[s] == b:
#         satisfied = 1
#     if s == e:
#         answer += str(satisfied)
#         return
#     for i in paths[s]:
#         if i != past:
#             pathfind(i, e, b, satisfied, s)

# f = open('milkvisits.in')
# line = f.readline()
# line = line.split()
# n, m = int(line[0]), int(line[1])
# breed = '0' + f.readline()
# paths = [[] for i in range(n+1)]
# for i in range(n-1):
#     line = f.readline()
#     line = line.split()
#     line = [int(i) for i in line]
#     paths[line[0]].append(line[1])
#     paths[line[1]].append(line[0])
# answer = ''
# for i in range(m):
#     line = f.readline()
#     line = line.split()
#     s, e, b = int(line[0]), int(line[1]), line[2]

#     pathfind(s, e, b, 0, 'null')
# #            start, end, breed, satisfied?, previousNode
# f.close()
# f = open('milkvisits.out', 'w')
# f.write(answer)
# f.close()



