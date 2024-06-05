def dfs(temp_group, start, curr):
    passed[curr] = True
    if exist[conversions[curr]]:
        if conversions[curr] == start:
            global group_num
            for i in temp_group:
                groups[i] = group_num
            group_addition.append(1)
            group_num += 1
            return
    
        if groups[conversions[curr]] != 'none':
            group_addition[groups[conversions[curr]]] = 0
        elif not passed[conversions[curr]]:
            dfs(temp_group+[curr], start, conversions[curr])


line = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = []
for i in line:
    alphabet.append(i)

T = int(input())
for t in range(T):
    line = input()
    start = [i for i in line]
    line = input()
    end = [i for i in line]
    n = len(start)

    #verify
    repeated = [[] for i in range(52)]
    for i in range(n):
        if end[i] not in repeated[alphabet.index(start[i])]:
            repeated[alphabet.index(start[i])].append(end[i])
    # print(repeated)
    # print('*'*20)
    if start == end:
        print(0)
        continue
    x = True
    y = False
    for i in repeated:
        if len(i) != 1:
            x = False
        if len(i) > 1:
            y = True
    if x or y:
        print(-1)
        # print(x,y)
        continue

    else:
        #calculate loops
        conversions = {}
        for i in range(n):
            if start[i] != end[i]:
                conversions[start[i]] = end[i]
        # print(conversions)
        ans = len(conversions)
        letters = conversions.keys()
        exist = {}
        for i in alphabet:
            exist[i] = False
        for i in letters:
            exist[i] = True
        passed = {}
        for i in letters:
            passed[i] = False
        groups = {}
        for i in letters:
            groups[i] = 'none'
        group_num = 1
        group_addition = [0]
        for i in letters:
            if passed[i] == False:
                dfs([i], i, i)
        # print(passed)
        # print(groups)
        # print(group_addition)
        print(ans+sum(group_addition))
