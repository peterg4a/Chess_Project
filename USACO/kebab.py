def calc(line):
    if len(line) == n:
        print(line)
        return
    if line[-1] == 0:
        calc(line+[1])
        calc(line+[0])
    else:
        calc(line+[0])

n = int(input())
calc([0])
calc([1])
