line = input()
line = line.split()
line = [int(i) for i in line]
n, Q = line

line = input()
fence = [0 for i in range(n)]
fence = [ord(i)-64 for i in line]

for i in range(Q):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    a, b = line
    for j in range(a-1, b):
        fence[j] = 0

    ans = 1
    passed = [False for i in range(27)]
    passed[0] = True
    for j in range(n-1):
        if fence[j] < fence[j+1]:
            passed[fence[j+1]] = True
            ans += 1
        if fence[j] > fence[j+1]:
            for a in range(fence[j+1]+1, 27, 1):
                passed[a] = False
            if not passed[fence[j+1]]:
                ans += 1
    print(ans)
