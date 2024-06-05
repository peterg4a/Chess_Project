n = int(input())
line = input()
line = line.split()
cows = [int(i) for i in line]
cows.sort()
line = input()
line = line.split()
rooms = [int(i) for i in line]
rooms.sort()
products = []
ans = 1
for i in range(n):
    cow = cows[-i-1]
    num = 0
    for j in rooms:
        if j >= cow:
            num += 1
    num -= i
    ans = ans * num
print(ans)