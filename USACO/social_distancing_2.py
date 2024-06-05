n = int(input())
cows = []
infected = []
for i in range(n):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    cows.append(line)
    if line[1] == 1:
        infected.append(line[0])
cows.sort()
R = 1000000
for i in range(n-1):
    cow = cows[i]
    next_cow = cows[i+1]
    if cow[1] != next_cow[1]:
        x = next_cow[0] - cow[0]
        R = min(x, R)

ans = 1
for i in range(len(infected) - 1):
    cow = infected[i]
    next_cow = infected[i+1]
    if next_cow - cow >= R:
        ans += 1
print(ans)
