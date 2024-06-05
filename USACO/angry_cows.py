def check():
    cows_used = 0
    start = 0
    for i in range(n):
        if hay_bales[i] > start:
            start = hay_bales[i] + mid*2
            cows_used += 1
    return(k >= cows_used)


line = input()
line = line.split()
n, k = int(line[0]), int(line[1])
hay_bales = []
for i in range(n):
    hay_bales.append(int(input()))
hay_bales.sort()

l, r = 0, hay_bales[-1]
while l+1 < r:
    mid = (l+r)//2

    if check():
        r = mid
    else:
        l = mid
print(r)

