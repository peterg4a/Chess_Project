# line = input()
# line = line.split()
# lawnmower_input = [int(i) for i in line]
# lawnmower_area_length = lawnmower_input[3] - lawnmower_input[1]
# lawnmower_area_width = lawnmower_input[2] - lawnmower_input[0]

# line = input()
# line = line.split()
# cow_feed_input = [int(i) for i in line]

# lawnmower = []
# for i in range(lawnmower_input[3] - lawnmower_input[1] + 1):
#     for j in range(lawnmower_input[2] - lawnmower_input[0] + 1):
#         point = [lawnmower_input[0] + j, lawnmower_input[1] + i]
#         lawnmower.append(point)

# overlap = []
# for i in range(cow_feed_input[3] - cow_feed_input[1] + 1):
#     for j in range(cow_feed_input[2] - cow_feed_input[0] + 1):
#         point = [cow_feed_input[0] + j, cow_feed_input[1] + i]
#         if point in lawnmower:
#             overlap.append(point)

# if len(overlap) != 0:
#     x1 = -1000
#     x2 = 1000
#     y1 = -1000
#     y2 = 1000
#     for i in range(len(overlap)):
#         point = overlap[i]
#         if point[0] > x1:
#             x1 = point[0]
#         if point[0] < x2:
#             x2 = point[0]
#         if point[1] > y1:
#             y1 = point[1]
#         if point[1] < y2:
#             y2 = point[1]

#     overlap_area_length = y1 - y2
#     overlap_area_width = x1 - x2
#     ans = lawnmower_area_length * lawnmower_area_width
#     if overlap_area_length == lawnmower_area_length or overlap_area_width == lawnmower_area_width:
#         ans = ans - overlap_area_length * overlap_area_width

# else:
#     ans = lawnmower_area_length * lawnmower_area_width

# print(ans)

f = open('billboard.in')
line = f.readline()
line = line.split()
lawnmower_input = [int(i) for i in line]
lawnmower_area_length = lawnmower_input[3] - lawnmower_input[1]
lawnmower_area_width = lawnmower_input[2] - lawnmower_input[0]
line = f.readline()
line = line.split()
cow_feed_input = [int(i) for i in line]
f.close()

lawnmower = []
for i in range(lawnmower_input[3] - lawnmower_input[1] + 1):
    for j in range(lawnmower_input[2] - lawnmower_input[0] + 1):
        point = [lawnmower_input[0] + j, lawnmower_input[1] + i]
        lawnmower.append(point)

overlap = []
for i in range(cow_feed_input[3] - cow_feed_input[1] + 1):
    for j in range(cow_feed_input[2] - cow_feed_input[0] + 1):
        point = [cow_feed_input[0] + j, cow_feed_input[1] + i]
        if point in lawnmower:
            overlap.append(point)

if len(overlap) != 0:
    x1 = -1000
    x2 = 1000
    y1 = -1000
    y2 = 1000
    for i in range(len(overlap)):
        point = overlap[i]
        if point[0] > x1:
            x1 = point[0]
        if point[0] < x2:
            x2 = point[0]
        if point[1] > y1:
            y1 = point[1]
        if point[1] < y2:
            y2 = point[1]

    overlap_area_length = y1 - y2
    overlap_area_width = x1 - x2
    ans = lawnmower_area_length * lawnmower_area_width
    if overlap_area_length == lawnmower_area_length or overlap_area_width == lawnmower_area_width:
        ans = ans - overlap_area_length * overlap_area_width

else:
    ans = lawnmower_area_length * lawnmower_area_width

f = open('billboard.out', 'w')
f.write(str(ans))
f.close()