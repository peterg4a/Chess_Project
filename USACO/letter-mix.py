def calc(k, used, line):
    if k == len(Line):
        print(line)
        return
    
    for i in range(n):
        if not used[i]:
            used[i] = True
            calc(k+1, used, line + Line[i] )
            used[i] = False

Line = input()
n = len(Line)
used = [False for i in range(n)]
calc(0, used, '')