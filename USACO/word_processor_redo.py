f = open('word.in')
line = f.readline()
line = line.split()
line = [int(i) for i in line]
n,k = line
words = f.readline()
words = words.split()
f.close()
line = words[0]
line_len = len(words[0])
f = open('word.out', 'w')
for i in range(1, n):
    if len(words[i]) + line_len <= k:
        line += ' ' + words[i]
        line_len += len(words[i])
    else:
        f.write(line+'\n')
        line = words[i]
        line_len = len(words[i])
f.write(line)