n = int(input())
cows = []
cows2 = []
Bessie = 'none'
for i in range(n):
    h = int(input())
    cows.append(h)
    cows2.append(h)
cows2.sort()

start = 'none'
end = 'none'
for i in range(n):
    if cows[i] != cows2[i] and start == 'none':
        start = i
    if cows[i] != cows2[i]:
        end = i
length = end - start

ans = 1
for i in range(length):
    a = cows[start + i]
    if i != 0:
        if a != previous:
            ans += 1
    previous = a
print(ans)