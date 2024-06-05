line = input()
line = line.split()
n = int(line[0])
k = int(line[1])
words = input()
words = words.split()

line = []
for i in range(n):
    character_number = 0
    if len(line) == 0:
        line.append(i)
    else:
        character_number = 0
        for a in range(len(line)):
            character_number = character_number + len(words[line[a]])
    
    if character_number + len(words[i]) < k:
        line.append(i)
    else:
        output = ''
        for a in range(len(line)):
            output = output + words[line[a]] + ' '
        print(output)
        line.clear()