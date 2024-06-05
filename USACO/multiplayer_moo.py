n = int(input())
Map = []
for i in range(n):
    line = input().split()
    line = [int(i) for i in line]
    Map.append(line)
groups = []
udlr = [[1,0],[0,1],[-1,0],[0,-1]]
passed = [[False for j in range(n)] for i in range(n)]
for Row in range(n):
    for Collumn in range(n):
        if passed[Row][Collumn] == False:
            to_be_passed = []
            to_be_passed.append([Row,Collumn])
            group = []
            passed[Row][Collumn] = True
            #modeling recursion with a list
            while len(to_be_passed) != 0:
                if len(to_be_passed) > n**2:
                    break
                # for i in passed:
                #     print(i)
                [row, collumn] = to_be_passed.pop(0)
                num = Map[row][collumn]
                group.append([row,collumn])

                for j in udlr:
                    new_row = row+j[0]
                    new_collumn = collumn+j[1]
                    if new_row<0 or new_row>n-1 or new_collumn<0 or new_collumn>n-1:
                        continue
                    if Map[new_row][new_collumn] == num and passed[new_row][new_collumn] == False:
                        to_be_passed.append([new_row,new_collumn])
                        passed[new_row][new_collumn] = True
            #finishing to_be_passed
            groups.append(group)
group_count = [len(i) for i in groups]
print(max(group_count))

for i in groups:
    print(i)

num_map = [[] for i in range(len(groups)+1)]
for i in groups:
    print(Map[i[0][0]][i[0][1]])
    num_map[Map[i[0][0]][i[0][1]]].append(len(i))
print(num_map)
touching = [[False for i in range(len(groups)+1)] for i in range(len(groups)+1)]

for row in range(n):
    for collumn in range(n):
        num = Map[row][collumn]
        for k in udlr:
            new_row = row+k[0]
            new_collumn = collumn+k[1]
            if new_row<0 or new_row>n-1 or new_collumn<0 or new_collumn>n-1:
                continue
            new_num = Map[new_row][new_collumn]
            touching[num][new_num] = True
            touching[new_num][num] = True
max_connect = 0
for i in range(len(touching)):
    for j in range(len(touching[i])):
        if touching[i][j] == True:
            connect = num_map[i]+num_map[j]
            if connect > max_connect:
                max_connect = connect
print(max_connect)