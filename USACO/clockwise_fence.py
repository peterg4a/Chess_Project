N = {'E' : 1, 'W' : -1}
S = {'W' : 1, 'E' : -1}
E = {'S' : 1, 'N' : -1}
W = {'N' : 1, 'S' : -1}
output = []
n = int(input())
for i in range(n):
    line = input()
    direction = 0
    for j in range(len(line) - 1):
        if line[j + 1] != line[j]:
            a = line[j + 1]
            if line[j] == 'N':
                direction += N[a]
            if line[j] == 'S':
                direction += S[a]
            if line[j] == 'E':
                direction += E[a]
            if line[j] == 'W':
                direction += W[a]
    if direction > 0:
        output.append('CW')
    else:
        output.append('CCW')
for i in output:
    print(i)