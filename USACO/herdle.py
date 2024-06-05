answer = ''
guess = ''
for i in range(3):
    answer += input()
for i in range(3):
    guess += input()

status = []
for i in range(9):
    status.append('none')

for i in range(9):
    if guess[i] == answer[i]:
        status[i] = 'green'
for i in range(9):
    if status[i] != 'green':
        for j in range(9):
            if guess[i] == answer[j] and status[j] != 'yellow' and status[j] != 'green':
                status[j] = 'yellow'
green = 0
yellow = 0
for i in range(9):
    if status[i] == 'green':
        green += 1
    if status[i] == 'yellow':
        yellow += 1
print(green)
print(yellow)