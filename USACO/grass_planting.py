def calc(node, prev):
    for i in range(1, 1000000000):
        valid = True
        for j in cnc[node]:
            if i == grass[j]:
                valid = False
                break
            for l in cnc[j]:
                if l != node and grass[l] == i:
                    valid = False
                    break
        print(node, i, valid)
        if valid:
            grass[node] = i
            break
    
    for i in cnc[node]:
        if i != prev:
            calc(i, node)



n = int(input())
cnc = []
for i in range(n+1):
    cnc.append([])
for i in range(n-1):
    line = input()
    line = line.split()
    a, b = [int(i) for i in line]
    cnc[a].append(b)
    cnc[b].append(a)
grass = []
for i in range(n+1):
    grass.append(False)

calc(1, 0)
print(cnc)
print(grass)
nums = []
ans = -1
for i in range(10**6):
    nums.append(False)
for i in grass:
    if nums[i] == False:
        ans += 1
        nums[i] = True
print(ans)