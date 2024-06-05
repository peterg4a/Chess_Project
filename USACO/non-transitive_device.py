#Is dice1 bigger than dice2?
def calc(dice1, dice2):
    W = 0
    L = 0
    for i in range(4):
        x = dice1[i]
        for j in range(4):
            if x > dice2[j]:
                W += 1
            if x < dice2[j]:
                L += 1
    if W > L:
        return True
    else:
        return False
n = int(input())
for i in range(n):
    line = input()
    line = line.split()
    line = [int(j) for j in line]
    dice1 = []
    dice2 = []
    for j in range(4):
        dice1.append(line[j])
        dice2.append(line[j+4])
    
    if not calc(dice1,dice2):
        dice2, dice1 = dice1, dice2

    ans = 'no'
    for a in range(1, 11, 1):
        for b in range(1, 11, 1):
            for c in range(1, 11, 1):
                for d in range(1, 11, 1):
                    dice3 = [a,b,c,d]
                    if calc(dice3, dice1) and  calc(dice2, dice3):
                        ans = 'yes'
    print(ans)