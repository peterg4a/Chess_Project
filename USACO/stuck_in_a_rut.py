# n = int(input())
# cows = []
# blocks = []
# for i in range(n):
#     blocks.append(0)
# dead_grass = []
# for i in range(n):
#     line = input()
#     line = line.split()
#     cows.append([line[0], int(line[1]), int(line[2])])

# for i in range(10):
#     for j in range(n):
#         if cows[j][0] != 'Stop':
#             cow = cows[j]

#             dead_grass.append([j, cow[1], cow[2]])

#             if cow[0] == 'N':
#                 cow[2] += 1
#             if cow[0] == 'E':
#                 cow[1] += 1
#             cows[j] = cow


#             for a in dead_grass:
#                 if a[1] == cow[1] and a[2] == cow[2]:
#                     cows[j][0] == 'Stop'
#                     blocks[a[0]] += 1

