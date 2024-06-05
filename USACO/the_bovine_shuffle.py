f = open('shuffle.in')
n = int(f.readline())

shuffle_input = f.readline()
shuffle_input = shuffle_input.split()
shuffle_input = [int(i) for i in shuffle_input]
shuffle = {}
for i in range(n):
    shuffle[shuffle_input.index(i + 1)] = i+1

cows = f.readline()
cows = cows.split()
f.close()
for i in range(3):
    i = i + 1
    new_cows = []
    for j in range(n):
        new_cows.append('none')
    for j in range(n):
        new_cows[j] = cows[shuffle[j]-1]
    cows = [i for i in new_cows]
f = open('shuffle.out', 'w')
for i in range(n):
    f.write(str(cows[i])+'\n')
f.close()