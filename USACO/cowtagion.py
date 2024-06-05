roads = []
n = int(input())
for i in range(n-1):
    line = input()
    line = line.split()
    roads.append([int(line[0]), int(line[1])])
ans = 0

node_roads = []
for i in range(n):
    node_roads.append(0)
for i in roads:
    node_roads[i[0] - 1] += 1
    node_roads[i[1] - 1] += 1

for i in range(n):
    this_node_road = node_roads[i]
    
    if i == 0:
        k = this_node_road + 1
    
    else:
        k = this_node_road

    num = 1
    while True:
        if num >= k:
            break
        ans += 1
        num = num * 2
    
    ans += (k-1)
print(ans)