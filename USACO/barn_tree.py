import math
import sys
sys.setrecursionlimit(100000000)
def recursion(prev_node, node):
    # print(prev_node,node)
    global orders
    for i in connections[node]:
        if i != prev_node:
            recursion(node, i)

    if prev_node != 'null':
        #code for the exchange
        if hays[node] > average_hay:
            orders.append([node, prev_node, hays[node]-average_hay])
            hays[prev_node] = hays[prev_node] + hays[node] - average_hay
        if hays[node] < average_hay:
            orders.append([prev_node, node, average_hay-hays[node]])
            hays[prev_node] = hays[prev_node] - average_hay + hays[node]

n = int(input())
line = input().split()
hays = [0]+[int(i) for i in line]
hays_copy = [i for i in hays]
#might not be integer
average_hay = math.floor(sum(hays)/n)
connections = [[] for i in range(n+1)]
for i in range(n-1):
    line = input().split()
    line = [int(i) for i in line]
    connections[line[0]].append(line[1])
    connections[line[1]].append(line[0])

orders = []
recursion('null', 1)
# print(orders)
hays = [i for i in hays_copy]
final_orders = []
used = [False for i in range(len(orders)+1)]
while len(final_orders) < len(orders):
    # print(final_orders)
    for i in range(len(orders)):
        order = orders[i]
        if hays[order[0]] - order[2] >= 0 and used[i]==False:
            hays[order[0]] -= order[2]
            hays[order[1]] += order[2]
            final_orders.append(order)
            used[i] = True

# print(final_orders)
print(len(final_orders))
for order in final_orders:
    line = str(order[0])+' '+str(order[1])+' '+str(order[2])
    print(line)