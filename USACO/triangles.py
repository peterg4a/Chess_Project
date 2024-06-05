# n = int(input())
# points = []
# for i in range(n):
#     line = input()
#     line = line.split()
#     points.append([int(line[0]), int(line[1])])

# max_area = 0
# for i in range(n):
#     max_y = 0
#     max_x = 0
#     point = points[i]
#     for j in range(n):
#         other_point = points[j]
#         if other_point[0] == point[0]:
#             if max_y < abs(other_point[1] - point[1]):
#                 max_y = abs(other_point[1] - point[1])
#         if other_point[1] == point[1]:
#             if max_x < abs(other_point[0] - point[0]):
#                 max_x = abs(other_point[0] - point[0])
#     if max_x * max_y > max_area:
#         max_area = max_x * max_y
#     print(max_x, max_y, max_area)
# print(max_area)

f = open('triangles.in')
n = int(f.readline())
points = []
for i in range(n):
    line = f.readline()
    line = line.split()
    points.append([int(line[0]), int(line[1])])
f.close()

max_area = 0
for i in range(n):
    max_y = 0
    max_x = 0
    point = points[i]
    for j in range(n):
        other_point = points[j]
        if other_point[0] == point[0]:
            if max_y < abs(other_point[1] - point[1]):
                max_y = abs(other_point[1] - point[1])
        if other_point[1] == point[1]:
            if max_x < abs(other_point[0] - point[0]):
                max_x = abs(other_point[0] - point[0])
    if max_x * max_y > max_area:
        max_area = max_x * max_y
    print(max_x, max_y, max_area)
f = open('triangles.out', 'w')
f.write(str(max_area))
f.close()