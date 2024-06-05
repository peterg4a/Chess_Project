def dfs(start, cnt, )


line = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = []
for i in line:
    alphabet.append(i)
print(len(alphabet))

T = int(input())
for t in range(T):
    start = input()
    end = input()
    n = len(start)

    repeated = [[] for i in range(52)]
    for i in range(n):
        repeated[alphabet.index(start[i])].append(end[i])
    x = True
    y = True
    for i in repeated:
        if i == []:
            x = False
        if len(i) > 1:
            y = False
    if not x or not y:
        print(-1)
        continue

    else:
        passed = [False for i in range(n)]
        for i in range(n):
            if not passed[i]:
                dfs()


    
