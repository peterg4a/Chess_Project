land = {}

for i in range(100):
    land[i + 1] = '.'
number = 1

for a in range(10):
    line = input()

    for b in range(10):
        land[number] = line[b]
        number = number + 1
        
time = 1
numbers = []
keep_going = 'yes'
while True:
    for i in range(100):
        position = i + 1
        if land[position] == 'C' or land[position] == 'B':
            #North
            if position + 10 >= 100:
                if land[position + 10] == '.':
                    numbers.append(position + 10)
                if land[position + 10] == 'L':
                    keep_going = 'no'
                    break
            
            #South
            if position - 10 < 0:
                if land[position - 10] == '.':
                    numbers.append(position - 10)
                if land[position - 10] == 'L':
                    keep_going = 'no'
                    break
            
            #East
            if position % 10 != 0:
                if land[position + 1] == '.':
                    numbers.append(position + 1)
                if land[position + 1] == 'L':
                    keep_going = 'no'
                    break

            #West
            if position % 10 != 1:
                if land[position - 1] == '.':
                    numbers.append(position - 1)
                if land[position - 1] == 'L':
                    keep_going = 'no'
                    break
    
    for i in range(len(numbers)):
        land[numbers[i]] = 'C'
    
    if keep_going == 'no':
        break
    
    time = time + 1

print(time)