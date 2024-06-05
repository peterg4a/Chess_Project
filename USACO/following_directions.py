import sys
sys.setrecursionlimit(5000)
def calc(Map, weight_map, n):
    ans = 0
    for i in range(n):
        ans += Map[i][-1] * weight_map[i][-1]
    for i in range(n):
        ans += Map[-1][i] * weight_map[-1][i]
    return ans

def p_recursion(val, row, col, prev):
    global weight_map
    if row <= n or col <= n:
        weight_map[row][col] += val
        if Map[row][col] == 'R':
            p_recursion(val, row, col+1, weight_map[row][col])
        if Map[row][col] == 'D':
            p_recursion(val, row+1, col, weight_map[row][col])
def n_recursion(val, row, col, prev):
    global weight_map
    if row <= n or col <= n:
        weight_map[row][col] -= val
        if Map[row][col] == 'R':
            n_recursion(val, row, col+1, weight_map[row][col])
        if Map[row][col] == 'D':
            n_recursion(val, row+1, col, weight_map[row][col])


n = int(input())
Map = []
for i in range(n):
    line = input().split()
    row = [j for j in line[0]]
    row.append(int(line[1]))
    Map.append(row)
line = input().split()
line = [int(i) for i in line]
Map.append(line)
# print(Map)

weight_map = [[1 for i in range(n)]+[0] for j in range(n)]+[[0 for k in range(n)]]
for row in range(n):
    for col in range(n):
        if Map[row][col] == 'R':
            weight_map[row][col+1] += weight_map[row][col]
        if Map[row][col] == 'D':
            weight_map[row+1][col] += weight_map[row][col]
# print(weight_map)

answers = []
answers.append(calc(Map, weight_map, n))
q = int(input())
for i in range(q):
    line = input().split()
    row, col = [int(i)-1 for i in line]
    if Map[row][col] == 'R':
        Map[row][col] = 'D'
        n_recursion(weight_map[row][col], row, col+1, weight_map[row][col])
        p_recursion(weight_map[row][col], row+1, col, weight_map[row][col])
    elif Map[row][col] == 'D':
        Map[row][col] = 'R'
        p_recursion(weight_map[row][col], row, col+1, weight_map[row][col])
        n_recursion(weight_map[row][col], row+1, col, weight_map[row][col])
    answers.append(calc(Map, weight_map, n))

for i in answers:
    print(i)