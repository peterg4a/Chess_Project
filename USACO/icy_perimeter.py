# def calc(x, y):
#     global area, perimeter
#     checked[x][y] = True
#     area += 1
#     for i in udlr:
#         xx = x+i[0]
#         yy = y+i[1]
#         if xx>=0 and xx<n and yy>=0 and yy<n:
#             if Map[xx][yy] == '.':
#                 perimeter += 1
#             if Map[xx][yy] == '#' and checked[xx][yy] == False:
#                 calc(xx, yy)
#         else:
#             perimeter += 1

# n = int(input())
# Map = []
# for i in range(n):
#     Map.append(input())

# checked = [[False for i in range(n)] for i in range(n)]
# udlr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# largest = [0, 0]
# for i in range(n):
#     for j in range(n):
#         if checked[i][j] == False and Map[i][j] == '#':
#             area = 0
#             perimeter = 0
#             calc(i, j)
#             print(area, perimeter)
#             if area > largest[0]:
#                 largest = [area, perimeter]
#             if area == largest[0]:
#                 largest[1] = min(perimeter, largest[1])
# print(largest[0], largest[1])



def calc(x, y):
    List = [[x, y]]
    global area, perimeter
    while len(List) > 0:
        x, y = List[0]
        if checked[x][y] == True:
            List.pop(0)
            continue
        checked[x][y] = True
        area += 1
        for i in udlr:
            xx = x+i[0]
            yy = y+i[1]
            if xx>=0 and xx<n and yy>=0 and yy<n:
                if Map[xx][yy] == '.':
                    perimeter += 1
                if Map[xx][yy] == '#' and checked[xx][yy] == False:
                    # print(xx, yy)
                    # print(checked[xx][yy])
                    List.append([xx, yy])
                    checked[x][y] = True
            else:
                perimeter += 1
        List.pop(0)

n = int(input())
Map = []
for i in range(n):
    Map.append(input())

checked = [[False for i in range(n)] for i in range(n)]
udlr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
largest = [0, 0]
for i in range(n):
    for j in range(n):
        if checked[i][j] == False and Map[i][j] == '#':
            area = 0
            perimeter = 0
            calc(i, j)
            # print('ans', area, perimeter)
            if area > largest[0]:
                largest = [area, perimeter]
            if area == largest[0]:
                largest[1] = min(perimeter, largest[1])
print(largest[0], largest[1])