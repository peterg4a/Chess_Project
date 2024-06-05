n = int(input())
line = input().split()
line = [int(i) for i in line]
passes = [[int(i/2), int(i/2)] for i in line]
direction = 'r'
position = 0
ans = ''
while True:
    if passes[0] == [0,0]:
        break
    if direction == 'r':
        if position == n:
            direction = 'l'
        elif passes[position][1] == 0:
            direction = 'l'
        else:
            ans += 'R'
            passes[position][1] -= 1
            position += 1
    elif direction == 'l':
        if position == 0:
            direction = 'r'
        elif position == n:
            passes[position-1][0] -= 1
            ans += 'L'
            position -= 1
        elif passes[position-1][1] < passes[position][1]:
            direction = 'r'
        else:
            passes[position-1][0] -= 1
            ans += 'L'
            position -= 1
print(ans)