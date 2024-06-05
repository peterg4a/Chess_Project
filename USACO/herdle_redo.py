answer = ''
guess = ''
for i in range(3):
    answer += input()
for i in range(3):
    guess += input()
answer_letters = {}
for i in answer:
    if i not in answer_letters:
        answer_letters[i] = 1
    else:
        answer_letters[i] += 1
green = 0
yellow = 0
for i in range(9):
    if guess[i] == answer[i]:
        green += 1
        answer_letters[answer[i]] -= 1
for i in range(9):
    if guess[i] != answer[i]:
        if guess[i] in answer_letters:
            if answer_letters[guess[i]] >0:
                yellow += 1
                answer_letters[guess[i]] -= 1
    
print(green)
print(yellow)