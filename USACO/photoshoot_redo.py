def calc(num):
    a = []
    a.append(num)
    for j in range(n-1):
        if b[j] - num > 0 and b[j] - num <= n:
            if not used[b[j] - num]:
                used[b[j] - num] = True
                num = b[j] - num
                a.append(num)
            else:
                return False
        else:
            return False
    return a

n = int(input())
line = input()
line = line.split()
b = [int(i) for i in line]
used = []
for i in range(n+1):
    used.append(False)

for i in range(1, b[0]):
    x = calc(i)
    if x != False:
        ans = ''
        for i in range(n-1):
            ans += str(x[i]) + ' '
        ans += str(x[-1])
        print(ans)
        break
    used = [False for i in used]
