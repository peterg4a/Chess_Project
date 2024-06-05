f = open('breedflip.in')
n = int(f.readline())
a = f.readline()
b = f.readline()
f.close()
ans = 0
for i in range(n-1):
    if a[i] != b[i] and a[i-1] == b[i-1]:
        ans = ans + 1

f = open('breedflip.out', 'w')
f.write(str(ans))
f.close()