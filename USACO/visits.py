n = int(input())
cows = []
for i in range(n):
    line = input()
    line = line.split()
    line = [int(j) for j in line]
    cows.append([line[1],line[0],True,i+1])

cows.sort(reverse=True)
print(cows)

value = 0
for i in cows:
    if cows[i[1]-1][2]:
        value += i[0]
        i[2] = False
        cows[i[3]-1][2] = False
        print(i,cows[i[1]-1])

print(cows)
print(value)
