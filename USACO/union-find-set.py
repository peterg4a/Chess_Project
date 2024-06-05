def find(x):
    if List[x] == x:
        return x
    else:
        List[x] = find(List[x])
        return List[x]

def union(a, b):
    a = find(a)
    b = find(b)
    List[b] = a

def isSame(a, b):
    return find(a) == find(b)

line = input()
line = line.split()
n, m = [int(i) for i in line]
List = [i for i in range(n+1)]
for i in range(m):
    line = input()
    line = line.split()
    line = [int(j) for j in line]
    if line[0] == 1:
        union(line[1], line[2])
    if line[0] == 2:
        if isSame(line[1], line[2]):
            print('Y')
        else:
            print('N')