f = open('circlecross.in')
line = f.readline()
f.close()
pairs = 0
crossings = []
used_letters = []
for i in range(52):
    crossings.append(line[i])

for i in range(52):
    if crossings[i] not in used_letters:
        used_letters.append(crossings[i])
        letter1_positions = []
        letter1 = crossings[i]
        for a in range(52):
            if crossings[a] == letter1:
                letter1_positions.append(a)
        
        crosses = []
        for a in range(abs(letter1_positions[0] - letter1_positions[1]) - 1):
            if crossings[i+a+1] not in crosses:
                crosses.append(crossings[i+a+1])
            else:
                crosses.remove(crossings[i+a+1])
        
        pairs = pairs + len(crosses)

f = open('circlecross.out', 'w')
f.write(str(int(pairs/2)))
f.close()