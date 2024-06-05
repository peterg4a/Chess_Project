cowphabet = input()
herd = input()
sum = 1
number = 0
for i in range(len(herd) - 1):
    letter = herd[i]
    next_letter = herd[i + 1]
    if cowphabet.find(next_letter) <= cowphabet.find(letter):
        sum = sum + 1

print(sum)