line = input()
line = line.split()
line = [int(i) for i in line]
c, n = line
chickens = []
for i in range(c):
    chickens.append(int(input()))
chickens.sort()

cows = []
for i in range(n):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    cows.append(line)
cows.sort(key = lambda x:(x[1], -x[0]))

ans = 0
cow_number = 0
chicken_number = 0
while cow_number < n and chicken_number < c:
    chicken = chickens[chicken_number]
    cow = cows[cow_number]
    if chicken >= cow[0] and chicken <= cow[1]:
        ans += 1
        cow_number += 1
        chicken_number += 1
    if chicken > cow[1]:
        cow_number += 1
    if cow[0] > chicken:
        chicken_number += 1

print(ans)