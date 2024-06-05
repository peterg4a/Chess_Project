both = {'Bessie' : 0, 'Maggie' : 0, 'Elsie' : 0, 'Gertie' : 0, 'Daisy' : 0, 'Annabelle' : 0, 'Henrietta' : 0}
second_last = []
f = open('notlast.in')
n = int(f.readline())
for i in range(n):
    line = f.readline()
    line = line.split()
    both[line[0]] += int(line[1])
f.close()
milk = list(both.values())
cows = list(both.keys())
least = 100000000
for i in milk:
    if i < least:
        least = i
second_least = 100000000
for i in milk:
    if i > least and i < second_least:
        second_least = i
for i in range(7):
    if milk[i] == second_least:
        second_last.append(cows[i])
f = open('notlast.out', 'w')
if len(second_last) != 1:
    f.write('Tie')
else:
    f.write(str(second_last[0]))
f.close()