n = int(input())
preferences = []
for i in range(n):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    preferences.append(line)

answers = []
for i in range(n+1):
    answers.append(0)

available = []
for i in range(n+1):
    available.append(True)

for i in range(n):
    for j in range(n):
        preference = preferences[j]
        for a in preference: