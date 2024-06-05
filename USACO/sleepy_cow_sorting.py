f = open('sleepy.in')
n = int(f.readline())
cows = (f.readline())
cows = cows.split()
cows = [int(i) for i in cows]
f.close()


starting_position = n - 1
for i in range(n):
    if cows[n - i - 1] > cows[n - i - 2]:
        starting_position = starting_position - 1
    
    else:
        break

f = open('sleepy.out', 'w')
f.write(str(starting_position))
f.close()
